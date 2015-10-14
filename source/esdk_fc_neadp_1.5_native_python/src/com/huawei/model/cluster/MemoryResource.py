'''
Created on 2015-3-7

@author: lWX232078
'''

class MemoryResource(object):
    '''
    classdocs
    '''
    totalSizeMB = None
    allocatedSizeMB = None


    def __init__(self, _totalSizeMB=None,_allocatedSizeMB=None):
        '''
        Constructor
        '''
        self.totalSizeMB = _totalSizeMB
        self.allocatedSizeMB = _allocatedSizeMB