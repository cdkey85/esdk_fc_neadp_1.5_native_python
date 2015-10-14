'''
Created on 2015-3-16

@author: sWX231817
'''

class VolumeBackInfo(object):
    '''
    classdocs
    '''
    urn = None
    uri = None
    uuid = None
    name = None
    createTime = None
    status = None
    storageType = None
    datastoreUrn = None
    datastoreName = None


    def __init__(self, _urn=None, _uri=None, _uuid=None, _name=None, _createTime=None, _status=None, _storageType=None, _datastoreUrn=None, _datastoreName=None):
        '''
        Constructor
        '''
        urn = _urn
        uri = _uri
        uuid = _uuid
        name = _name
        createTime = _createTime
        status = _status
        storageType = _storageType
        datastoreUrn = _datastoreUrn
        datastoreName = _datastoreName        
