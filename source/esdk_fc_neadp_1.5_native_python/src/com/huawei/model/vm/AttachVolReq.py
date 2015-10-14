'''
Created on 2015-3-6

@author: sWX231817
'''

class AttachVolReq(object):
    '''
    classdocs
    '''
    volUrn = None
    pciType = None
    sequenceNum = None


    def __init__(self, _volUrn=None, _pciType=None, _sequenceNum=None):
        '''
        Constructor
        '''
        self.volUrn = _volUrn
        self.pciType = _pciType
        self.sequenceNum = _sequenceNum        
