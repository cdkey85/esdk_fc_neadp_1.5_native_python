'''
Created on 2015-3-6

@author: sWX231817
'''

class AddNicReq(object):
    '''
    classdocs
    '''
    name = None
    portGroupUrn = None
    mac = None
    sequenceNum = None
    virtIo = None

    def __init__(self, _name=None, _portGroupUrn=None, _mac=None, _sequenceNum=None, _virtIo=None):
        '''
        Constructor
        '''
        self.name = _name
        self.portGroupUrn = _portGroupUrn
        self.mac = _mac
        self.sequenceNum = _sequenceNum
        self.virtIo = _virtIo        
