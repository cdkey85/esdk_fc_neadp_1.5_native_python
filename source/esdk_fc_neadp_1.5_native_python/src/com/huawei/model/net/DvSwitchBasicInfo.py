'''
Created on 2015-3-16

@author: lWX232078
'''

class DvSwitchBasicInfo(object):
    '''
    classdocs
    '''
    urn = None
    uri = None
    name = None
    description = None
    type = None
    portGroupNum = None
    isIgmpSnooping = None

    def __init__(self,
                     _urn = None,
                    _uri = None,
                    _name = None,
                    _description = None,
                    _type = None,
                    _portGroupNum = None,
                    _isIgmpSnooping = None,):
        '''
        Constructor
        '''
        self.urn = _urn
        self.uri = _uri
        self.name = _name
        self.description = _description
        self.type = _type
        self.portGroupNum = _portGroupNum
        self.isIgmpSnooping = _isIgmpSnooping