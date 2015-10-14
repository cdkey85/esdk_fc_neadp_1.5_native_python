'''
Created on 2015-3-16

@author: sWX231817
'''

import Datastore

class QueryDatastoreListResp(object):
    '''
    classdocs
    '''
    total = None
    datastores = [None]

    def __init__(self, _total=None,_datastores=[None]):
        '''
        Constructor
        '''
        self.total = _total
        self.datastores = _datastores