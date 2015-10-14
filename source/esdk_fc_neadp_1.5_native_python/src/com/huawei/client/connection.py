# =========================================================================
# Copyright 2012-present Yunify, Inc.
# -------------------------------------------------------------------------
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this work except in compliance with the License.
# You may obtain a copy of the License in the LICENSE file, or at:
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========================================================================

import time
import random
import threading
import httplib
import urllib
import json
import auth
from json_tool import dict2object
from com.huawei.model.common.SDKCommonResp import SDKCommonResp
from com.huawei.client.log4py import log_config
from com.huawei.client.log import *

class ConnectionQueue(object):
    """
    Http connection queue
    """

    def __init__(self, timeout=60):
        self.queue = []
        self.timeout = timeout

    def size(self):
        return len(self.queue)

    def get_conn(self):
        # get a valid connection or `None`
        for _ in range(len(self.queue)):
            (conn, _) = self.queue.pop(0)
            if self._is_conn_ready(conn):
                return conn
            else:
                self.put_conn(conn)

    def put_conn(self, conn):
        self.queue.append((conn, time.time()))

    def clear(self):
        # clear expired connections
        while self.queue and self._is_conn_expired(self.queue[0]):
            self.queue.pop(0)

    def _is_conn_expired(self, conn_info):
        (_, time_stamp) = conn_info
        return (time.time() - time_stamp) > self.timeout

    def _is_conn_ready(self, conn):
        # sometimes the response may not be remove
        # after read at lasttime's connection
        response = getattr(conn, '_HTTPConnection__response', None)
        return (response is None) or response.isclosed()


class ConnectionPool(object):
    """
    Http connection pool for multiple hosts.
    It's thread-safe
    """

    CLEAR_INTERVAL = 5.0

    def __init__(self, timeout=60):
        self.timeout = timeout
        self.last_clear_time = time.time()
        self.lock = threading.Lock()
        self.pool = {}

    def size(self):
        with self.lock:
            return sum([conn.size() for conn in self.pool.values()])

    def put_conn(self, host, is_secure, conn):
        # put connection into host's connection pool
        with self.lock:
            key = (host, is_secure)
            queue = self.pool.setdefault(key, ConnectionQueue(self.timeout))
            queue.put_conn(conn)

    def get_conn(self, host, is_secure):
        # get connection from host's connection pool
        # return a valid connection or `None`
        self._clear()
        with self.lock:
            key = (host, is_secure)
            if key in self.pool:
                return self.pool[key].get_conn()

    def _clear(self):
        # clear expired connections of all hosts
        with self.lock:
            curr_time = time.time()
            if self.last_clear_time + self.CLEAR_INTERVAL > curr_time:
                return
            key_to_delete = []
            for key in self.pool:
                self.pool[key].clear()
                if self.pool[key].size() == 0:
                    key_to_delete.append(key)
            for key in key_to_delete:
                del self.pool[key]
            self.last_clear_time = curr_time


class HTTPRequest(object):

    def __init__(self, method, protocol, header, host, port, path,
                 params, body=""):
        """
        Represents an HTTP request.

        @param method - The HTTP method name, 'GET', 'POST', 'PUT' etc.
        @param protocol - 'http' or 'https'
        @param header - http request header
        @param host - the host to make the connection to
        @param port - the port to use when connect to host
        @param path - URL path that is being accessed.
        @param auth_path - The part of the URL path used when creating the
                         authentication string.
        @param params - HTTP url query parameters, {'name':'value'}.
        @param body - Body of the HTTP request. If not present, will be None or
                     empty string ('').
        """
        self.method = method
        self.protocol = protocol
        self.header = header
        self.host = host
        self.port = port
        self.path = path
        self.auth_path = path
        self.params = params
        self.body = body

    def __str__(self):
        return (('method:(%s) protocol:(%s) header(%s) host(%s) port(%s) path(%s) '
                 'params(%s) body(%s)') % (self.method, self.protocol, self.header,
                                           self.host, str(self.port),
                                           self.path, self.params,
                                           self.body))

    def authorize(self, connection, **kwargs):
        # add authorize information to request
        connection._auth_handler.add_auth(self, **kwargs)


class HttpConnection(object):
    """
    Connection control to restful service
    """

    def __init__(self, qy_access_key_id, qy_secret_access_key, zone,
            host='172.22.4.4', port=7443, protocol='https',
            pool=None, expires=None,
            retry_time=3, http_socket_timeout=10):
        """
        @param qy_access_key_id - the access key id
        @param qy_secret_access_key - the secret access key
        @param zone - the zone id to access
        @param host - the host to make the connection to
        @param port - the port to use when connect to host
        @param protocol - the protocol to access to web server, "http" or "https"
        @param pool - the connection pool
        @param retry_time - the retry_time when message send fail
        """
        self.host = host
        self.port = port
        self.qy_access_key_id = qy_access_key_id
        self.qy_secret_access_key = qy_secret_access_key
        self.zone = zone.lower().strip()
        self.retry_time = retry_time
        self.http_socket_timeout = http_socket_timeout
        self._conn = pool if pool else ConnectionPool()
        self.expires = expires
        self.protocol = protocol
        self.secure = protocol.lower() == "https"
        self._auth_handler = auth.QuerySignatureAuthHandler(
                self.host,
                self.qy_access_key_id,
                self.qy_secret_access_key,
                )

    def _get_conn(self):
        # get connection from pool
        conn = self._conn.get_conn(self.host, self.secure)
        return conn or self._new_conn()

    def _set_conn(self, conn):
        # set valid connection into pool
        self._conn.put_conn(self.host, self.secure, conn)

    def _new_conn(self):
        if self.secure:
            return httplib.HTTPSConnection(self.host, self.port,
                    timeout=self.http_socket_timeout)
        else:
            return httplib.HTTPConnection(self.host, self.port,
                    timeout=self.http_socket_timeout)

    def _build_http_request(self, url, base_params, verb):
        params = {}
        for key, values in base_params.items():
            if values is None:
                continue
            if isinstance(values, list):
                for i in range(1, len(values) + 1):
                    if isinstance(values[i - 1], dict):
                        for sk, sv in values[i - 1].items():
                            params['%s.%d.%s' % (key, i, sk)] = sv
                    else:
                        params['%s.%d' % (key, i)] = values[i - 1]
            else:
                params[key] = values

        return HTTPRequest(verb, self.protocol, "", self.host, self.port, url,
                 params)

    def send(self, url, params, verb='GET'):
        request = self._build_http_request(url, params, verb)
        conn = self._get_conn()
        retry_time = 0
        while retry_time < self.retry_time:
            # Use binary exponential backoff to desynchronize client requests
            next_sleep = random.random() * (2 ** retry_time)
            try:
                if verb == "POST":
                    request.authorize(self)
                    conn.request(verb, request.path, request.body, request.header)
                else:
                    request.authorize(self)
                    conn.request(verb, request.path, request.body)
                response = conn.getresponse()
                if response.status == 200:
                    self._set_conn(conn)
                    return response.read()
                else:
                    conn = self._get_conn()
            except:
                if retry_time < self.retry_time - 1:
                    conn = self._get_conn()
                else:
                    raise
            time.sleep(next_sleep)
            retry_time += 1
    '''        
    def sendTo(self, method, url, body=None, headers={}):
        conn = self._get_conn()
        headersK = {}
        headersK['X-Auth-User']='fc01'
        headersK['X-Auth-Key']='36135da9586652aa0bdefee628001c4c4eb6901e278a44233a23cd2811eadc19'
        headersK['Accept']= 'application/json;charset=UTF-8;version=5.0;'
        #headersK['X-HW-Cloud-Auth-Token']='793481C3-0B4C-40D6-B932-C1F9DC2F9BD10'
        #headersK['X-AUTH-USER-ID']='5da4038a-2a84-416d-b706-85ccabca2780'
        headersK['user-agent']='HttpClient'
        headersK['Content-Type']='application/json;charset=UTF-8'
        headersK['X-Auth-Token']='0DCCC508-62AC-4DED-B815-E48485D1F8D80'
        
        #body = {name":"stri"}
        
        #body['name']='stri'
        aaaa = {}
        aaaa.name = 'Clusters1'
        body1 = json.dumps(aaaa.__dict__)
        #test_data_urlencode = urllib.urlencode(body)
        #conn.request('POST', 'https://172.22.4.4:7443/service/session', None, headersK)
        #https://172.22.4.4:7443/service/sites/4D9D0815/clusters/79
        #https://172.22.4.4:7443/service/sites/4D9D0815/volumes/875
        conn.request('GET', 'https://172.22.4.4:7443/service/sites', None, headersK)
        
        response = conn.getresponse()

        strResp = response.read()
        
        strRespChang = strResp.replace('":false','":False').replace('":true','":True')
        
        dictResp = eval(strRespChang)
        
        obj = dict2object(dictResp)
        
        return obj
    '''
    
class Singleton(object):  
    def __new__(cls, *args, **kw):  
        if not hasattr(cls, '_instance'):  
            orig = super(Singleton, cls)  
            cls._instance = orig.__new__(cls, *args, **kw)  
        return cls._instance   
         
class RestClient(Singleton):
    
    headersK = {}
    headersK['X-Auth-User'] = ''
    headersK['X-Auth-Key'] = ''
    headersK['Accept'] = 'application/json;charset=UTF-8;version=5.0'
    headersK['user-agent'] = 'HttpClient'
    headersK['Content-Type'] = 'application/json;charset=UTF-8'
    headersK['X-Auth-Token'] = ''
    
    conn = None
    host = ''
    port = 7443
    protocol = ''
    httpConnection = None
    
    def __init__(self):
        pass

    def connetToServer(self, host, port=7443, protocol='https'):
        self.host = host
        self.port = port
        self.protocol = protocol
        self.httpConnection = HttpConnection(qy_access_key_id='1',
                       qy_secret_access_key='1',
                       zone='1',
                       host=host, port=port, protocol=protocol)
        pass
    
    def send(self, method, url, body=None, resp=None, name=None):
        conn = self.httpConnection._get_conn()
        resp = SDKCommonResp()
        if not (url.find("/") == 0):
            url = "/" + url
        if(body == None):
            conn.request(method=method,
                     url=self.protocol + '://' + self.host + ':' + str(self.port) + url,
                     body=None,
                     headers=self.headersK)
        else:
            conn.request(method=method,
                     url=self.protocol + '://' + self.host + ':' + str(self.port) + url,
                     body=json.dumps(body),
                     headers=self.headersK)    
        response = conn.getresponse()
        if(url == '/service/session' and method == 'POST' and response.status == 200) :

            respHeaders = response.getheaders()
            self.loginSet(respHeaders[2][1])
        strResp = response.read()
        if  strResp.find("<") != 2 :
            if not strResp.count("errorCode", 0, len(strResp)) :
                strResp = strResp.rstrip('}') + ",%s}" % (str(resp.__dict__).rstrip('}').lstrip('{'))
                if not strResp.index(",", 0 , len(strResp)) :
                    strResp = "{" + strResp.lstrip(',')
                if strResp.index(",", 0 , len(strResp)) == 1 :
                    strResp = "{" + strResp.lstrip('{,')
            strRespChang = strResp.replace('":false', '":False').replace('":true', '":True').replace('":null', '":None')
            __log_resp = strRespChang
            dictResp = eval(strRespChang)
        else:
            resp.errorCode = "2130000404"
            dictResp = resp.__dict__
            __log_resp = dictResp
        __log_url = self.protocol + '://' + self.host + ':' + str(self.port) + urllib.unquote(url)
        __log_body = body
        __log_name = name
        # print name
#         log_config(__log_name, __log_url, __log_body, __log_resp)
        LOG(DEBUG, '[%s]:url={%s}\nbody={%s}\nresp={%s}', __log_name, __log_url, __log_body, __log_resp)
        # obj = dict2object(dictResp)
        return dictResp
        pass
    
    def loginSet(self, token):
        self.headersK['X-Auth-Token'] = token
        pass
    
    
    def sendTest(self):
        conn = self.httpConnection._get_conn()
        from com.huawei.model.common.Monitor import QueryObjectmetricReq
        queryObjectmetricReq = QueryObjectmetricReq()
        queryObjectmetricReq.urn = 'urn:sites:3EBE06F9:datastores:1'
        queryObjectmetricReq.metricId = ['cpu_usage', 'cpu_usage']
        # queryObjectmetricReq.metricId[0] = 'cpu_usage'
        # queryObjectmetricReq.metricId[1] = 'mem_usage'
    
        body = [None, None]
        body[0] = queryObjectmetricReq.__dict__
        body[1] = queryObjectmetricReq.__dict__
        # body[1] = queryObjectmetricReq.__dict__
    
        print json.dumps(body)
    
        conn.request(method='POST',
                     url='https://172.22.4.4:7443/service/sites/4D9D0815/monitors/objectmetric-realtimedata',
                     body=json.dumps(body),
                     headers=self.headersK)    
        
        response = conn.getresponse()
        
        strResp = response.read()
        strRespChang = strResp.replace('":false', '":False').replace('":true', '":True').replace('":null', '":None')
        dictResp = eval(strRespChang)
        # obj = dict2object(dictResp)
        return dictResp
        pass
        
