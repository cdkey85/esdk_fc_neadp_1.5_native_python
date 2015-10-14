'''
Created on 2015-3-7

@author: lWX232078
'''

class VolumeResp(object):
    '''
    classdocs
    '''
    urn = None
    uri = None
    taskUrn = None
    taskUri = None


    def __init__(self, _urn = None,_uri = None,_taskUrn = None,_taskUri = None):
        '''
        Constructor
        '''
        self.urn = _urn
        self.uri = _uri
        self.taskUri = _taskUri
        self.taskUrn = _taskUrn