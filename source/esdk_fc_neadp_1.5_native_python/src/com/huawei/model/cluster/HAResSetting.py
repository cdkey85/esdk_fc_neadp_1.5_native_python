'''
Created on 2015-3-7

@author: lWX232078
'''

class HAResSetting(object):
    '''
    classdocs
    '''
    isControlPolicy = None
    controlPolicy = None
    cpuReservation = None
    memoryReservation = None
    hostsFaultQuantity = None
    isCustomisedSlot = None
    slotcpuinmhz = None
    slotmeminmb = None
    failoverHosts = None
    isAutoMigrateAllVms = None
    inHaHostAutonomy = None
    hbDataStorePolicy = None
    hbDataStorePreferred = None
    hbDataStoreNumber = None
    isolateArbitrateAddress = None


    def __init__(self,
    _isControlPolicy = None,
    _controlPolicy = None,
    _cpuReservation = None,
    _memoryReservation = None,
    _hostsFaultQuantity = None,
    _isCustomisedSlot = None,
    _slotcpuinmhz = None,
    _slotmeminmb = None,
    _failoverHosts = None,
    _isAutoMigrateAllVms = None,
    _inHaHostAutonomy = None,
    _hbDataStorePolicy = None,
    _hbDataStorePreferred = None,
    _hbDataStoreNumber = None,
    _isolateArbitrateAddress = None):
        '''
        Constructor
        '''
        self.isControlPolicy = _isControlPolicy
        self.controlPolicy = _controlPolicy
        self.cpuReservation = _cpuReservation
        self.memoryReservation = _memoryReservation
        self.hostsFaultQuantity = _hostsFaultQuantity
        self.isCustomisedSlot = _isCustomisedSlot
        self.slotcpuinmhz = _slotcpuinmhz
        self.slotmeminmb = _slotmeminmb
        self.failoverHosts = _failoverHosts
        self.isAutoMigrateAllVms = _isAutoMigrateAllVms
        self.inHaHostAutonomy = _inHaHostAutonomy
        self.hbDataStorePolicy = _hbDataStorePolicy
        self.hbDataStorePreferred = _hbDataStorePreferred
        self.hbDataStoreNumber = _hbDataStoreNumber
        self.isolateArbitrateAddress = _isolateArbitrateAddress
        
        