'''
Created on 2015-3-7

@author: lWX232078
'''

class DpmThresholds(object):
    '''
    classdocs
    '''
    limen = None
    underloadThreshold = None
    overloadThreshold = None


    def __init__(self, _limen = None,_underloadThreshold = None,_overloadThreshold = None):
        '''
        Constructor
        '''
        self.limen = _limen
        self.underloadThreshold = _underloadThreshold
        self.overloadThreshold = _overloadThreshold