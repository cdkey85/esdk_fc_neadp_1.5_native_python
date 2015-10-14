# coding=utf-8
'''
Created on 2015-3-9

@author: lWX232078
'''

import urllib

from com.huawei.client.connection import RestClient
from com.huawei.model.storage.Datastore import Datastore
from com.huawei.model.storage.DatastoreQueryParams import DatastoreQueryParams
from com.huawei.model.storage.ModifyVolumeReq import ModifyVolumeReq
from com.huawei.model.storage.RemoveVolumeResp import RemoveVolumeResp
from com.huawei.model.storage.VolumeCreateParams import VolumeCreateParams
from com.huawei.model.storage.VolumeQueryParams import VolumeQueryParams
from com.huawei.model.storage.VolumeResp import VolumeResp
from com.huawei.model.storage.QueryDatastoreListResp import QueryDatastoreListResp
from com.huawei.model.storage.QueryDatastoreVolumeListReq import QueryDatastoreVolumeListReq
from com.huawei.model.storage.QueryDatastoreVolumeResp import QueryDatastoreVolumeResp
from com.huawei.model.storage.QueryVolumeListResp import QueryVolumeListResp

from com.huawei.model.storage.CreateVolBackReq import CreateVolBackReq
from com.huawei.model.storage.CreateVolBackResp import CreateVolBackResp
from com.huawei.model.storage.QueryVolBackResp import QueryVolBackResp
from com.huawei.model.storage.QueryVolumeResp import QueryVolumeResp
from com.huawei.model.storage.ResumeVolReq import ResumeVolReq
from com.huawei.model.vm.AsynchrTask import AsynchrTask
from com.huawei.client.utils import dict


class DataStorageResource(object):
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
    
    def queryDataStore(self, datastore_uri):
        '''
        function:查询指定数据存储
        '''
        response = client.send(method='GET', url=datastore_uri, body=None, resp=Datastore(), name="queryDataStore")
        return response
    
    
    def queryDataStoreList(self, site_uri, req=DatastoreQueryParams()):
        '''
        function:查询站点/主机/集群下所有数据存储
        '''
        site_uri += '/datastores'
        
        reqEx = dict(req)
        if reqEx:
            site_uri += "?" + urllib.urlencode(reqEx).replace("%5B", "").replace("%3A", ":").replace("%27", "").replace("%2C+", "").replace("%5D", "")
        response = client.send(method='GET', url=site_uri, body=None, resp=QueryDatastoreListResp(), name="queryDataStoreList")
        return response
    
    def createVolume(self, site_uri, req=VolumeCreateParams()):
        '''
        function:创建卷
        '''
        site_uri += '/volumes'
        reqEx = dict(req)
        response = client.send(method='POST', url=site_uri, body=reqEx, resp=VolumeResp(), name="createVolume")
        return response
    
    def removeVolume(self, vol_uri, isFormat=0):
        '''
        function:删除卷
        '''
        if isFormat == None:
            isFormat = 0
            pass
        vol_uri += '?isFormat=%d' % (isFormat)
        response = client.send(method='DELETE', url=vol_uri, body=None, resp=RemoveVolumeResp(), name="removeVolume")
        return response
    
    def queryVolume(self, vol_uri, refreshflag=None):
        '''
        function:查询指定卷
        '''
        url = vol_uri
        if not refreshflag == None:
            url += "?refreshflag=%s" % (str(refreshflag).lower())
        response = client.send(method='GET', url=url, body=None, resp=QueryVolumeResp(), name="queryVolume")
        return response
    
    def modifyVolume(self, vol_uri, req=ModifyVolumeReq()):
        '''
        function:修改指定卷
        '''
        reqEx = dict(req)
        response = client.send(method='PUT', url=vol_uri, body=reqEx, resp=None, name="modifyVolume")
        return response
    
    def queryVolumeList(self, site_uri, req=VolumeQueryParams()):
        '''
        function:分页查询卷列表
        '''
        site_uri += '/volumes'
        reqEx = dict(req)
        if reqEx:
            site_uri += "?" + urllib.urlencode(reqEx).replace("%5B", "").replace("%3A", ":").replace("%27", "").replace("%2C+", "&volUrns=").replace("%5D", "").replace("+", "")
        response = client.send(method='GET', url=site_uri, body=None, resp=QueryVolumeListResp(), name="queryVolumeList")
        return response
     
    def queryDatastoreVolumeList(self, site_uri, req=QueryDatastoreVolumeListReq()): 
        '''
        function:分页根据DataStore查询所有卷
        '''
        site_uri += '/volumes/querydatastorevolumes'  
                    
        reqEx = dict(req)
        if reqEx:
            site_uri += "?" + urllib.urlencode(reqEx).replace("%5B", "").replace("%3A", ":").replace("%27", "").replace("%2C+", "").replace("%5D", "").replace("+", "")
        response = client.send(method='GET', url=site_uri, body=None, resp=QueryDatastoreVolumeResp(), name="queryDatastoreVolumeList")
        return response
        
    def createVolBackup(self, vol_uri, req=CreateVolBackReq()): 
        '''
        function:创建卷备份
        '''
        url = vol_uri + '/backup '  
        reqEx = dict(req)
        response = client.send(method='POST', url=url, body=reqEx, resp=CreateVolBackResp(), name="createVolBackup")
        return response
    
    def queryVolBackup(self, vol_uri): 
        '''
        function:查询指定卷的备份
        '''
        url = vol_uri + '/querybackup'  
                    
        response = client.send(method='GET', url=url, body=None, resp=QueryVolBackResp(), name="queryVolBackup")
        return response
    
    def resumeVolBackup(self, vol_uri, req=ResumeVolReq()): 
        '''
        function:恢复指定卷备份
        '''
        url = vol_uri + '/resumevolume'  
        reqEx = dict(req)
        response = client.send(method='PUT', url=url, body=reqEx, resp=AsynchrTask(), name="resumeVolBackup")
        return response
        
