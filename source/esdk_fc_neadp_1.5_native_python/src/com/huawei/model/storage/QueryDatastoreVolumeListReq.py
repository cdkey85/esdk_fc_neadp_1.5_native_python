'''
Created on 2015-3-16

@author: sWX231817
'''

class QueryDatastoreVolumeListReq(object):
    '''
    classdocs
    '''
    limit = None
    offset = None
    dsUrn = None


    def __init__(self, _limit=0, _offset=0, _dsUrn=''):
        '''
        Constructor
        '''
        self.limit = _limit
        self.offset = _offset
        self.dsUrn = _dsUrn
        
