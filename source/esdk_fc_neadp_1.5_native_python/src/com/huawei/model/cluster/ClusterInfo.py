# coding=utf-8
'''
Created on 2015-3-6

@author: lWX232078
'''

import DrsExtensionConfig
import HAResSetting
import DRSSetting
import DrsVmConfig
from com.huawei.model.common.SDKCommonResp import SDKCommonResp

class ClusterInfo(SDKCommonResp):
    '''
    classdocs
    '''
    urn = None
    uri = None
    name = None
    parentObjUrn = None
    description = None
    tag = None
    isMemOvercommit = None
    isEnableHa = None
    haResSetting = None
    isEnableDrs = None
    drsSetting = None
    drsExtensionConfig = [None]
    statistics = None
    resStrategy = None
    isEnableImc = None
    imcSetting = None
    maxCpuQuantity = None
    enableVmDrs = None
    drsVmConfig = [None]
    enableGuestNuma = None
    enableIOTailor = None

    def __init__(self,
    _urn=None,
    _uri=None,
    _name=None,
    _parentObjUrn=None,
    _description=None,
    _tag=None,
    _isMemOvercommit=None,
    _isEnableHa=None,
    _haResSetting=None,
    _isEnableDrs=None,
    _drsSetting=None,
    _drsExtensionConfig=[None],
    _statistics=None,
    _resStrategy=None,
    _isEnableImc=None,
    _imcSetting=None,
    _maxCpuQuantity=None,
    _enableVmDrs=None,
    _drsVmConfig=[None],
    _enableGuestNuma=None,
    _enableIOTailor=None):
        
        '''
        Constructor
        '''
        self.uri = _uri
        self.urn = _urn
        self.name = _name
        self.parentObjUrn = _parentObjUrn
        self.description = _description
        self.tag = _tag
        self.isMemOvercommit = _isMemOvercommit
        self.isEnableHa = _isEnableHa
        self.haResSetting = _haResSetting
        self.isEnableDrs = _isEnableDrs
        self.drsSetting = _drsSetting
        self.drsExtensionConfig = _drsExtensionConfig
        self.statistics = _statistics
        self.resStrategy = _resStrategy
        self.isEnableImc = _isEnableImc
        self.imcSetting = _imcSetting
        self.maxCpuQuantity = _maxCpuQuantity
        self.enableVmDrs = _enableVmDrs
        self.drsVmConfig = _drsVmConfig
        self.enableGuestNuma = _enableGuestNuma
        self.enableIOTailor = _enableIOTailor
        
