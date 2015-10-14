# coding=utf-8
'''
Created on 2015-3-9

@author: lWX232078
'''
import urllib
from com.huawei.client.connection import RestClient
from com.huawei.model.net.PortGroup import PortGroup
from com.huawei.model.net.QueryPortGroupListReq import QueryPortGroupListReq
from com.huawei.model.net.QueryPortGroupListResp import QueryPortGroupListResp
from com.huawei.client.utils import dict

class PortGroupResource(object):
    '''
    classdocs
    '''
    global client
    client = RestClient()

    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def queryPortGroup(self, portgroup_uri):
        '''
        function:查询DVSwitch下指定的PortGroup
        '''
        response = client.send(method='GET', url=portgroup_uri, body=None, resp=PortGroup(), name="queryPortGroup")
        return response
    
    def queryPortGroupList(self, dvswitch_uri, req=QueryPortGroupListReq()):
        '''
        function:查询DVSwitch下所有的PortGroup
        '''
        dvswitch_uri += '/portgroups'
        reqEx = dict(req)
        if reqEx:
            dvswitch_uri += "?" + urllib.urlencode(reqEx).replace("%5B", "").replace("%3A", ":").replace("%27", "").replace("%2C+", "").replace("%5D", "")  
        response = client.send(method='GET', url=dvswitch_uri, body=None, resp=QueryPortGroupListResp(), name="queryPortGroupList")
        return response
    
    
        
    
