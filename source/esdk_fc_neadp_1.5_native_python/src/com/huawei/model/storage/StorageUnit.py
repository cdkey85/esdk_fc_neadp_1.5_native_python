'''
Created on 2015-3-7

@author: lWX232078
'''

class StorageUnit(object):
    '''
    classdocs
    '''
    urn = None
    suName = None
    sdName = None


    def __init__(self, _urn = None,_suName = None,_sdName = None):
        '''
        Constructor
        '''
        self.urn = _urn
        self.suName = _suName
        self.sdName = _sdName