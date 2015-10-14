'''
Created on 2015-3-6

@author: sWX231817
'''

class ModifyNicReq(object):
    '''
    classdocs
    '''
    name = None
    portGroupUrn = None
    mac = None


    def __init__(self, _name=None, _portGroupUrn=None, _mac=None):
        '''
        Constructor
        '''
        self.name = _name
        self.portGroupUrn = _portGroupUrn
        self.mac = _mac
