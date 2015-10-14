'''
Created on 2015-3-7

@author: lWX232078
'''

class QueryPortGroupListReq(object):
    '''
    classdocs
    '''
    limit=None
    offset=None
    portGroupName = None

    def __init__(self, _limit=None,_offset=None,_portGroupName=None):
        '''
        Constructor
        '''
        self.limit = _limit
        self.offset = _offset
        self.portGroupName = _portGroupName