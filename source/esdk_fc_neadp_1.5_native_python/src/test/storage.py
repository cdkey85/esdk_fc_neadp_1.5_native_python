# coding=utf-8
import sys 
sys.path.append("..")

from com.huawei.resources.common.AuthenticateResource import AuthenticateResource
from com.huawei.client.connection import RestClient
from com.huawei.resources.storage.DataStorageResource import DataStorageResource
from com.huawei.model.storage.DatastoreQueryParams import DatastoreQueryParams
from com.huawei.model.storage.VolumeCreateParams import VolumeCreateParams
from com.huawei.model.storage.ModifyVolumeReq import ModifyVolumeReq
from com.huawei.model.storage.VolumeQueryParams import VolumeQueryParams
from com.huawei.model.storage.QueryDatastoreVolumeListReq import QueryDatastoreVolumeListReq
from com.huawei.model.storage.QueryDatastoreVolumeResp import QueryDatastoreVolumeResp
from com.huawei.model.storage.CreateVolBackReq import CreateVolBackReq
from com.huawei.model.storage.ResumeVolReq import ResumeVolReq
from com.huawei.client.log import *

dataStorage = DataStorageResource()

def QueryDataStore():
    print '-------------queryDataStore start--------------------------------'
    datastore_uri = '/service/sites/4D9D0815/datastores/1'
    b = dataStorage.queryDataStore(datastore_uri)
    print b
    pass


def QueryDataStoreList():
    print '-------------------queryDataStoreList start------------------------'
    req = DatastoreQueryParams()
    req.limit =1 
    req.offset = 0
    site_uri = '/service/sites/4D9D0815'
    b = dataStorage.queryDataStoreList(site_uri, req)
    print b
    pass

def CreateVolume():
    print '-------------------createVolume start-----------------------------'
    req = VolumeCreateParams()
    req.name = 'VOltest1'
    req.quantityGB = 2
    req.datastoreUrn = 'urn:sites:4D9D0815:datastores:1'
    req.type = 'normal'
    site_uri = '/service/sites/4D9D0815'
    b = dataStorage.createVolume(site_uri, req)
    print b
    pass

def RemoveVolume():
    print '-------------------removeVolume start-----------------------------'
    vol_uri = '/service/sites/4D9D0815/volumes/940'
    b = dataStorage.removeVolume(vol_uri, isFormat=0)
    print b
    pass
def QueryVolume():
    print '-------------------removeVolume start-----------------------------'
    vol_uri = '/service/sites/4D9D0815/volumes/1091'
    b = dataStorage.queryVolume(vol_uri=vol_uri, refreshflag=True)
    print b
    pass

def ModifyVolume():
    print '-------------------modifyVolume start-----------------------------'
    req = ModifyVolumeReq()
    req.name = 'VOLTest2'
    vol_uri = '/service/sites/4D9D0815/volumes/940'
    b = dataStorage.modifyVolume(vol_uri, req)
    print b

def QueryVolumeList():
    print '-------------------queryVolumeList start--------------------------'
    req = VolumeQueryParams()
    req.limit = 10
    req.offset = 0
    site_uri = '/service/sites/4D9D0815'
    req.volUrns =['urn:sites:4D9D0815:volumes:1023','urn:sites:4D9D0815:volumes:1022']
    b = dataStorage.queryVolumeList(site_uri, req)
    print b
    pass

def QueryDatastoreVolumeList():
    print '-------------------queryDatastoreVolumeList start------------------'
    req = QueryDatastoreVolumeListReq()
    req.limit = 10
    req.offset = 0
    req.dsUrn = 'urn:sites:4D9D0815:datastores:1'
    site_uri = '/service/sites/4D9D0815'
    b = dataStorage.queryDatastoreVolumeList(site_uri, req)
    print b
    pass




def createVolBackup():
    req = CreateVolBackReq()
    req.datastoreUrn="urn:sites:4D9D0815:datastores:1"
    req.name="ccc"
    b = dataStorage.createVolBackup("/service/sites/4D9D0815/volumes/1046", req)
    print b
    pass




def queryVolBackup():
    b = dataStorage.queryVolBackup("/service/sites/4D9D0815/volumes/1046")
    print b
    pass
def resumeVolBackup():
    req = ResumeVolReq()
    req.datastoreUrn="urn:sites:4D9D0815:datastores:1"
    req.isQuickResume = True
    b = dataStorage.resumeVolBackup("/service/sites/4D9D0815/volumes/1046", req)
    print b
    pass




if __name__ == '__main__':
    client = RestClient()
    client.connetToServer(host='172.22.4.4', port=7443, protocol='https')
    login = AuthenticateResource()
    aaa = login.login('fc01', 'Huawei@123')
    QueryVolumeList()
