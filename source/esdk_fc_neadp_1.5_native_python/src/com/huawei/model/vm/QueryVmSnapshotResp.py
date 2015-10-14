'''
Created on 2015-3-10

@author: sWX231817
'''

from com.huawei.model.vm.VolSnapshot import VolSnapshot


class QueryVmSnapshotResp(object):
    '''
    classdocs
    '''
    urn = None
    uri = None
    name = None
    type = None
    description = None
    createTime = None
    status = None
    snapProvisionSize = None
    coreNum = None
    memorySize = None
    volumeSizeSum = None
    includingMemorySnapshot = None
    volsnapshots = [None]


    def __init__(self, _urn=None, _uri=None, _name=None, _type=None, _description=None, _createTime=None, _status=None,
                  _snapProvisionSize=None, _coreNum=None, _memorySize=None, _volumeSizeSum=None, _includingMemorySnapshot=None,
                   _volsnapshots=VolSnapshot()):
        '''
        Constructor
        '''
        urn = None
        uri = None
        name = None
        type = None
        description = None
        createTime = None
        status = None
        snapProvisionSize = None
        coreNum = None
        memorySize = None
        volumeSizeSum = None
        includingMemorySnapshot = None
        volsnapshots = None
