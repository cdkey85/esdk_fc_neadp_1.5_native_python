# coding=utf-8
'''
Created on 2015-3-16

@author: lWX232078
'''

import urllib
from com.huawei.client.connection import RestClient
from com.huawei.model.site.SiteBasicInfo import SiteBasicInfo


class SiteResource(object):
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
    
    def querySiteList(self): 
        '''
        function:查询站点列表
        '''
        response = client.send(method='GET', url='/service/sites', body=None, resp=[SiteBasicInfo()], name="querySiteList")
        return response 
