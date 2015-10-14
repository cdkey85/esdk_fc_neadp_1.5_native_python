'''
Created on 2015-3-13

@author: sWX231817
'''

class DeleteVmReq(object):
    '''
    classdocs
    '''
    isReserveDisks = None
    isFormat = None
    holdTime = None


    def __init__(self, _isReserveDisks=None, _isFormat=None, _holdTime=None):
        '''
        Constructor
        '''
        self.isReserveDisks = _isReserveDisks
        self.isFormat = _isFormat
        self.holdTime = _holdTime
