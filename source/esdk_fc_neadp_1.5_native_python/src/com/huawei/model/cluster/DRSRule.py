'''
Created on 2015-3-7

@author: lWX232078
'''
import Vms

class DRSRule(object):
    '''
    classdocs
    '''
    operationType = None
    ruleIndex = None
    ruleName = None
    ruleType = None
    vm2HostRuleType = None
    vms = None
    vmGroupUrn = None
    hostGroupUrn = None
    createTime = None
    updateTime = None


    def __init__(self, _operationType = None,
        _ruleIndex = None,
        _ruleName = None,
        _ruleType = None,
        _vm2HostRuleType = None,
        _vms = None,
        _vmGroupUrn = None,
        _hostGroupUrn = None,
        _createTime = None,
        _updateTime = None):
        '''
        Constructor
        '''
        self.operationType = _operationType
        self.ruleIndex = _ruleIndex
        self.ruleName = _ruleName
        self.ruleType = _ruleType
        self.vm2HostRuleType = _vm2HostRuleType
        self.vms = _vms
        self.vmGroupUrn = _vmGroupUrn
        self.hostGroupUrn = _hostGroupUrn
        self.createTime = _createTime
        self.updateTime = _updateTime