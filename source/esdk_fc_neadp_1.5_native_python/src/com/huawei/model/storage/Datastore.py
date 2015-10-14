'''
Created on 2015-3-7

@author: lWX232078
'''
import StorageUnit


class Datastore(object):
    '''
    classdocs
    '''
    urn = None
    uri = None
    suUrn = None
    suName = None
    storageType = None
    clusterSize = None
    name = None
    status = None
    capacityGB = None
    usedSizeGB = None
    freeSizeGB = None
    isThin = None
    thinRate = None
    actualCapacityGB = None
    actualFreeSizeGB = None
    refreshTime = None
    description = None
    hosts = [None]
    version = None
    ioDelay = None
    expandCount = None
    suIdList = [None]
    siocFlag = None
    storageUnits = [None]


    def __init__(self, _urn = None,
        _uri = None,
        _suUrn = None,
        _suName = None,
        _storageType = None,
        _clusterSize = None,
        _name = None,
        _status = None,
        _capacityGB = None,
        _usedSizeGB = None,
        _freeSizeGB = None,
        _isThin = None,
        _thinRate = None,
        _actualCapacityGB = None,
        _actualFreeSizeGB = None,
        _refreshTime = None,
        _description = None,
        _hosts = [None],
        _version = None,
        _ioDelay = None,
        _expandCount = None,
        _suIdList = [None],
        _siocFlag = None,
        _storageUnits = [None]):
        '''
        Constructor
        '''
        self.urn = _urn
        self.uri = _uri
        self.suUrn = _suUrn
        self.suName = _suName
        self.storageType = _storageType
        self.clusterSize = _clusterSize
        self.name = _name
        self.status = _status
        self.capacityGB = _capacityGB
        self.usedSizeGB = _usedSizeGB
        self.freeSizeGB = _freeSizeGB
        self.isThin = _isThin
        self.thinRate = _thinRate
        self.actualCapacityGB = _actualCapacityGB
        self.actualFreeSizeGB = _actualFreeSizeGB
        self.refreshTime = _refreshTime
        self.description = _description
        self.hosts = _hosts
        self.version = _version
        self.ioDelay = _ioDelay
        self.expandCount = _expandCount
        self.suIdList = _suIdList
        self.siocFlag = _siocFlag
        self.storageUnits = _storageUnits