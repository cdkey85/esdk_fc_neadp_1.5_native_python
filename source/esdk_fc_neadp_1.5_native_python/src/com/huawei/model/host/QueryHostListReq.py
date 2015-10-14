'''
Created on 2015-3-7

@author: lWX232078
'''

class QueryHostListReq(object):
    '''
    classdocs
    '''
    limit = None
    offset = None
    scope = None
    name = None
    ip = None
    resourceGroupFlag = None


    def __init__(self, _limit = None,_offset=None,_scope=None,_name=None,_ip=None,_resourceGroupFlag=None):
        '''
        Constructor
        '''
        self.limit = _limit
        self.offset = _offset
        self.scope = _scope
        self.name =_name
        self.ip = _ip
        self.resourceGroupFlag = _resourceGroupFlag