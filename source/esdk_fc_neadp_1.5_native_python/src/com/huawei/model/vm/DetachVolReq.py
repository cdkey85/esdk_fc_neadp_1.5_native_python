'''
Created on 2015-3-6

@author: sWX231817
'''

class DetachVolReq(object):
    '''
    classdocs
    '''
    volUrn = None
    isFormat = None

    def __init__(self, _volUrn=None, _isFormat=None):
        '''
        Constructor
        '''
        self.volUrn = _volUrn
        self.isFormat = _isFormat        
