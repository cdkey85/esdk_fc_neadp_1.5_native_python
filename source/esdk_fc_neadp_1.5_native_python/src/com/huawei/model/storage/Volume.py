'''
Created on 2015-3-7

@author: lWX232078
'''

class Volume(object):
    '''
    classdocs
    '''
    urn = None
    uri = None
    uuid = None
    name = None
    quantityGB = None
    status = None
    storageType = None
    isThin = None
    type = None
    datastoreUrn = None
    datastoreName = None
    indepDisk = None
    persistentDisk = None
    volNameOnDev = None
    volProvisionSize = None
    userUsedSize = None
    isDiffVol = None
    volType = None
    maxReadBytes = None
    maxWriteBytes = None
    maxReadRequest = None
    maxWriteRequest = None
    pciType = None
    occupiedVolume = None
    bindToVm = None
    srcVolumeUrn = None
    volumeUseType = None
    ioWeight = None
    siocFlag = None
    volumeUrl = None
    linkCloneParent = None



    def __init__(self, 
                _urn = None,
                _uri = None,
                _uuid = None,
                _name = None,
                _quantityGB = None,
                _status = None,
                _storageType = None,
                _isThin = None,
                _type = None,
                _datastoreUrn = None,
                _datastoreName = None,
                _indepDisk = None,
                _persistentDisk = None,
                _volNameOnDev = None,
                _volProvisionSize = None,
                _userUsedSize = None,
                _isDiffVol = None,
                _volType = None,
                _maxReadBytes = None,
                _maxWriteBytes = None,
                _maxReadRequest = None,
                _maxWriteRequest = None,
                _pciType = None,
                _occupiedVolume = None,
                _bindToVm = None,
                _srcVolumeUrn = None,
                _volumeUseType = None,
                _ioWeight = None,
                _siocFlag = None,
                _volumeUrl = None,
                _linkCloneParent = None):
        '''
        Constructor
        '''
        self.urn = _urn
        self.uri = _uri
        self.uuid = _uuid
        self.name = _name
        self.quantityGB = _quantityGB
        self.status = _status
        self.storageType = _storageType
        self.isThin = _isThin
        self.type = _type
        self.datastoreUrn = _datastoreUrn
        self.datastoreName = _datastoreName
        self.indepDisk = _indepDisk
        self.persistentDisk = _persistentDisk
        self.volNameOnDev = _volNameOnDev
        self.volProvisionSize = _volProvisionSize
        self.userUsedSize = _userUsedSize
        self.isDiffVol = _isDiffVol
        self.volType = _volType
        self.maxReadBytes = _maxReadBytes
        self.maxWriteBytes = _maxWriteBytes
        self.maxReadRequest = _maxReadRequest
        self.maxWriteRequest = _maxWriteRequest
        self.pciType = _pciType
        self.occupiedVolume = _occupiedVolume
        self.bindToVm = _bindToVm
        self.srcVolumeUrn = _bindToVm
        self.volumeUseType = _volumeUseType
        self.ioWeight = _ioWeight
        self.siocFlag = _siocFlag
        self.volumeUrl = _volumeUrl
        self.linkCloneParent = _linkCloneParent