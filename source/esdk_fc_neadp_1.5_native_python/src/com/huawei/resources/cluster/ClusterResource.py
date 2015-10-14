# coding=utf-8
'''
Created on 2015-3-7

@author: lWX232078
'''
import urllib

from com.huawei.client.connection import RestClient
from com.huawei.model.cluster.ClusterBasicInfo import ClusterBasicInfo
from com.huawei.model.cluster.ClusterInfo import ClusterInfo
from com.huawei.model.cluster.QueryClusterListReq import QueryClusterListReq
from com.huawei.client.utils import dict

class ClusterResource(object):
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
    
    def queryCluster(self, cluster_uri):
        '''
        function:查询cluster信息
        '''
        response = client.send(method='GET', url=cluster_uri, body=None, resp=ClusterInfo(), name="queryCluster")
        return response
    
    
    
    def  queryClusterList(self, site_uri, req=QueryClusterListReq()):
        '''
        function:过滤查询所有Cluster
        '''
         
        site_uri += '/clusters'        
        reqEx = dict(req)
        if reqEx:        
            site_uri += "?" + urllib.urlencode(reqEx).replace("%5B", "").replace("%3A", ":").replace("%27", "").replace("%2C+", "&clusterUrns=").replace("%5D", "").replace("+", "")    
        response = client.send(method='GET', url=site_uri, body=None, resp=[ClusterBasicInfo()], name="queryClusterList")
        return response
    
    
