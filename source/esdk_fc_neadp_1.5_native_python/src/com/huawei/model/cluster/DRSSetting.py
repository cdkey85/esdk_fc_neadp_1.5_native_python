#coding=utf-8

'''
Created on 2015-3-7

@author: lWX232078
'''
import DrsCycle
import DpmThreshold
import DpmThresholds
import FragmentLimen
import DRSRule

class DRSSetting(object):
    '''
    classdocs
    '''
    drsLevel = None
    drsFragmentLimen = None
    drsCycle = None
    drsRules = None
    powerLevel = None
    powerLimen = None
    powerFragmentLimen = None
    dpmCycle = None
    factor = None
    drsThreshold = None
    dpmThresholds = None
    electricStrategy = None



    def __init__(self,_drsLevel = None,
    _drsFragmentLimen = None,
    _drsCycle = None,
    _drsRules = None,
    _powerLevel = None,
    _powerLimen = None,
    _powerFragmentLimen = None,
    _dpmCycle = None,
    _factor = None,
    _drsThreshold = None,
    _dpmThresholds = None,
    _electricStrategy = None):
        '''
        Constructor
        '''
        self.drsLevel = _drsLevel
        self.drsFragmentLimen = _drsFragmentLimen
        self.drsCycle = _drsCycle
        self.drsRules = _drsRules
        self.powerLevel = _powerLevel
        self.powerLimen = _powerLimen
        self.powerFragmentLimen = _powerFragmentLimen
        self.dpmCycle = _dpmCycle
        self.factor = _factor
        self.drsThreshold = _drsThreshold
        self.dpmThresholds = _dpmThresholds
        self.electricStrategy = _electricStrategy       