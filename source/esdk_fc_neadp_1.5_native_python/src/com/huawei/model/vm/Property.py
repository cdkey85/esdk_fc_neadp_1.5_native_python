'''
Created on 2015-3-6

@author: sWX231817
'''

class Property(object):
    '''
    classdocs
    '''
    bootOption = None
    isEnableHa = None
    vmFaultProcess = None
    reoverByHost = None
    clockMode = None
    isEnableMemVol = None
    isEnableFt = None
    isAutoUpgrade = None
    attachType = None
    gpuShareType = None    
    isReserveResource = None
    secureVmType = None
    isHpet = None


    def __init__(self, _bootOption=None, _isEnableHa=None, _vmFaultProcess=None, _reoverByHost=None, _clockMode=None,
                  _isEnableMemVol=None, _isEnableFt=None, _isAutoUpgrade=None, _attachType=None, _gpuShareType=None,
                   _isReserveResource=None, _secureVmType=None, _isHpet=None):
        '''
        Constructor
        '''
        self.bootOption = _bootOption
        self.isEnableHa = _isEnableHa
        self.vmFaultProcess = _vmFaultProcess
        self.reoverByHost = _reoverByHost
        self.clockMode = _clockMode
        self.isEnableMemVol = _isEnableMemVol
        self.isEnableFt = _isEnableFt
        self.isAutoUpgrade = _isAutoUpgrade
        self.attachType = _attachType
        self.gpuShareType = _gpuShareType    
        self.isReserveResource = _isReserveResource
        self.secureVmType = _secureVmType
        self.isHpet = _isHpet
