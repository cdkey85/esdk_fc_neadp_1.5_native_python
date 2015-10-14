# coding=utf-8
'''
Created on 2015-3-9

@author: lWX232078
'''
import urllib
from com.huawei.client.connection import RestClient
from com.huawei.model.host.QueryHostListReq import QueryHostListReq
from com.huawei.model.host.QueryHostListResp import QueryHostListResp
from com.huawei.model.host.HostInfo import HostInfo
from com.huawei.client.utils import dict

class HostResource(object):
    '''
    classdocs
    '''
    global client
    client = RestClient();

    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def queryHostList(self, site_uri, req=QueryHostListReq()):
        '''
        function:查询主机列表
        req=QueryHostListReq()
        '''
        site_uri += '/hosts'
        reqEx = dict(req)
        if reqEx:
            site_uri += "?" + urllib.urlencode(reqEx).replace("%5B", "").replace("%3A", ":").replace("%27", "").replace("%2C+", "").replace("%5D", "")    
        response = client.send(method='GET', url=site_uri, body=None, resp=QueryHostListResp(), name="queryHostList")
        return response
    
    def queryHost(self, host_uri):
        '''
        function:查询指定主机
        '''
        response = client.send(method='GET', url=host_uri, body=None, resp=HostInfo(), name="queryHost")
        return response
