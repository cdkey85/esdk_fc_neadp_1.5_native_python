'''
Created on 2015-3-7

@author: lWX232078
'''

class CpuResource(object):
    '''
    classdocs
    '''
    totalSizeMHz = None
    allocatedSizeMHz = None


    def __init__(self,_totalSizeMHz=None,_allocatedSizeMHz=None ):
        '''
        Constructor
        '''
        self.totalSizeMHz = _totalSizeMHz
        self.allocatedSizeMHz = _allocatedSizeMHz