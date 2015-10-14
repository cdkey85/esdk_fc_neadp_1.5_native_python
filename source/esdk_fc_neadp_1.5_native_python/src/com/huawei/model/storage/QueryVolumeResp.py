'''
Created on 2015-3-16

@author: sWX231817
'''

class QueryVolumeResp(object):
    '''
    classdocs
    '''
    urn = None
    uri = None
    name = None
    quantityGB = None
    status = None
    storageType = None
    isThin = None
    type = None
    datastoreUrn = None
    datastoreName = None
    sdUrn = None
    sdUri = None
    uuid = None
    volNameOnDev = None
    iscsi = None
    indepDisk = None
    persistentDisk = None
    volProvisionSize = None
    userUsedSize = None
    isDiffVol = None
    volType = None
    maxReadBytes = None
    maxWriteBytes = None
    maxReadRequest = None
    maxWriteRequest = None
    pciType = None

    def __init__(self, _urn=None, _uri=None, _name=None, _quantityGB=None, _status=None, _storageType=None, _isThin=None, _type=None,
                  _datastoreUrn=None, _datastoreName=None, _sdUrn=None, _sdUri=None, _uuid=None, _volNameOnDev=None, _iscsi=None,
                   _indepDisk=None, _persistentDisk=None, _volProvisionSize=None, _userUsedSize=None, _isDiffVol=None, _volType=None,
                    _maxReadBytes=None, _maxWriteBytes=None, _maxReadRequest=None, _maxWriteRequest=None, _pciType=None):
        '''
        Constructor
        '''
        self.urn = _urn
        self.uri = _uri
        self.name = _name
        self.quantityGB = _quantityGB
        self.status = _status
        self.storageType = _storageType
        self.isThin = _isThin
        self.type = _type
        self.datastoreUrn = _datastoreUrn
        self.datastoreName = _datastoreName
        self.sdUrn = _sdUrn
        self.sdUri = _sdUri
        self.uuid = _uuid
        self.volNameOnDev = _volNameOnDev
        self.iscsi = _iscsi
        self.indepDisk = _indepDisk
        self.persistentDisk = _persistentDisk
        self.volProvisionSize = _volProvisionSize
        self.userUsedSize = _userUsedSize
        self.isDiffVol = _isDiffVol
        self.volType = _volType
        self.maxReadBytes = _maxReadBytes
        self.maxWriteBytes = _maxWriteBytes
        self.maxReadRequest = _maxReadRequest
        self.maxWriteRequest = _maxWriteRequest
        self.pciType = _pciType
