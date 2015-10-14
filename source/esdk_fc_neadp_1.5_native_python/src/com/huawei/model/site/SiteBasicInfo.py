'''
Created on 2015-3-16

@author: lWX232078
'''

class SiteBasicInfo(object):
    '''
    classdocs
    '''
    urn = None
    uri = None
    name = None
    ip = None
    isDC = None
    isSelf = None
    status = None

    def __init__(self,
                    _urn = None,
                    _uri = None,
                    _name = None,
                    _ip = None,
                    _isDC = None,
                    _isSelf = None,
                    _status = None,):
        '''
        Constructor
        '''
        self.urn = _urn
        self.uri = _uri
        self.name = _name
        self.ip = _ip
        self.isDC = _isDC
        self.isSelf = _isSelf
        self.status = _status