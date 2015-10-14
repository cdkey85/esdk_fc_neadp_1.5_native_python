'''
Created on 2015-3-16

@author: sWX231817
'''

from com.huawei.model.storage.VolumeBackInfo import VolumeBackInfo

class QueryVolBackResp(object):
    '''
    classdocs
    '''

    volumes = [VolumeBackInfo()]
    def __init__(self, _volumes=None):
        '''
        Constructor
        '''
        self.volumes = _volumes