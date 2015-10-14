# coding=utf-8
'''
Created on 2015-3-6

@author: y00206201
'''
from com.huawei.client.connection import RestClient
from com.huawei.model.common.LoginResp import LoginResp
import hashlib

class AuthenticateResource(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def login(self, username, password):
        '''
        input:username:用户名，password:密码
        function:登陆
        '''
        client = RestClient()
        client.headersK['X-Auth-User'] = username
        client.headersK['X-Auth-Key'] = str(hashlib.sha256(password).hexdigest())
        # client.headersK['X-Auth-Key']='36135da9586652aa0bdefee628001c4c4eb6901e278a44233a23cd2811eadc19'
        result = client.send(method='POST', url='/service/session', body=None, resp=LoginResp(), name="login")
        return result
        pass
     
    def logout(self):
        '''
        function:退出
        '''
        client = RestClient()
        result = client.send(method='DELETE', url='/service/session', body=None, resp=None, name="logout")
        return result
        pass   
