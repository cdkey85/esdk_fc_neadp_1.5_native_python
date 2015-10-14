'''
Created on 2015-3-16

@author: sWX231817
'''

import Volume
import QueryDatastoreVolumeResp

class QueryVolumeListResp(object):
    '''
    classdocs
    '''
    total = None
    volumes = [None]  # queryVolumeList:Volume->queryVolumeList,queryDatastoreVolumeList:Volume->QueryDatastoreVolumeResp
                    
    def __init__(self, _total=None, _volumes=[None]):
        '''
        Constructor
        '''
        self.total = _total
        self.volumes = _volumes
