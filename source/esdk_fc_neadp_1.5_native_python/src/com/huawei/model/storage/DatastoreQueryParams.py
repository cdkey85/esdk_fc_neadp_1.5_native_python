'''
Created on 2015-3-7

@author: lWX232078
'''


class DatastoreQueryParams(object):
    '''
    classdocs
    '''
    limit=None
    offset=None
    scope=None
    status=None
    name=None
    exceptDatastoreType=None


    def __init__(self, _limit=None,_offset=None,_scope=None,_status=None,_name=None,_exceptDatastoreType=None):
        '''
        Constructor
        '''
        self.limit=_limit
        self.offset=_offset
        self.scope=_scope
        self.status=_status
        self.name=_name
        self.exceptDatastoreType=_exceptDatastoreType