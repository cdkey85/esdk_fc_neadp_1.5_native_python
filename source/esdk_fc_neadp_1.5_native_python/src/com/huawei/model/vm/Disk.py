'''
Created on 2015-3-6

@author: sWX231817
'''

class Disk(object):
    '''
    classdocs
    '''
    pciType = None
    sequenceNum = None
    volumeUrn = None
    volumeUuid = None
    quantityGB = None
    isDataCopy = None
    datastoreUrn = None
    isThin = None
    indepDisk = None
    persistentDisk = None
    storageType = None
    volType = None
    maxReadBytes = None
    maxWriteBytes = None
    maxReadRequest = None
    maxWriteRequest = None
    type = None
    diskName = None
    ioWeight = None
    datastoreName = None


    def __init__(self, _pciType=None, _sequenceNum=None, _volumeUrn=None, _volumeUuid=None, _quantityGB=None, _isDataCopy=None,
                  _datastoreUrn=None, _isThin=None, _indepDisk=None, _persistentDisk=None, _storageType=None, _volType=None,
                   _maxReadBytes=None, _maxWriteBytes=None, _maxReadRequest=None, _maxWriteRequest=None, _type=None, _diskName=None,
                    _ioWeight=None, _datastoreName=None):
        '''
        Constructor
        '''
        self.pciType = _pciType
        self.sequenceNum = _sequenceNum
        self.volumeUrn = _volumeUrn
        self.volumeUuid = _volumeUuid
        self.quantityGB = _quantityGB
        self.isDataCopy = _isDataCopy
        self.datastoreUrn = _datastoreUrn
        self.isThin = _isThin
        self.indepDisk = _indepDisk
        self.persistentDisk = _persistentDisk
        self.storageType = _storageType
        self.volType = _volType
        self.maxReadBytes = _maxReadBytes
        self.maxWriteBytes = _maxWriteBytes
        self.maxReadRequest = _maxReadRequest
        self.maxWriteRequest = _maxWriteRequest
        self.type = _type
        self.diskName = _diskName
        self.ioWeight = _ioWeight
        self.datastoreName = _datastoreName
        
