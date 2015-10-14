'''
Created on 2015-3-7

@author: lWX232078
'''

class VolumeQueryParams(object):
    '''
    classdocs
    '''
    limit = None
    offset = None
    scope = None
    volUrns = None
    name = None
    refreshflag = None
    pciType = None
    drFlag = None
    attachstatus = None



    def __init__(self,     
        _limit = None,
        _offset = None,
        _scope = None,
        _volUrns = None,
        _name = None,
        _refreshflag = None,
        _pciType = None,
        _drFlag = None,
        _attachstatus = None):
        '''
        Constructor
        '''
        self.limit = _limit
        self.offset = _offset
        self.scope = _scope
        self.volUrns = _volUrns
        self.name = _name
        self.refreshflag = _refreshflag
        self.pciType = _pciType
        self.drFlag = _drFlag
        self.attachstatus = _attachstatus