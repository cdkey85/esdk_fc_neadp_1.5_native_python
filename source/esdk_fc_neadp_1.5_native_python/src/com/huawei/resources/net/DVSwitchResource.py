#coding=utf-8
'''
Created on 2015-3-16

@author: lWX232078
'''

import urllib
from com.huawei.client.connection import RestClient
from com.huawei.model.net.DvSwitchBasicInfo import DvSwitchBasicInfo
 

class DVSwitchResource(object):
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
    
    def queryDVSwitchList(self,site_uri,location=None,name=None):
        '''
        function:查询所有的DVSwitch信息
        location:location为clusterUrn 或 hostUrn
        name:DVSwitch名称
        '''
       
        dvswitch_uri = site_uri + '/dvswitchs' + '?'
  
        if location:
            dvswitch_uri += 'location=' + str(location) + '&'
            pass
        if name:
            dvswitch_uri += 'name=' + str(name) + '&'
            pass
        
        dvswitch_uri = dvswitch_uri[:-1] 
        
        response = client.send(method='GET', url=dvswitch_uri, body=None, resp=[DvSwitchBasicInfo()], name="queryDVSwitchList")
        return response  
               
            
       