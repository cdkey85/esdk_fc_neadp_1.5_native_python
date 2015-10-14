'''
Created on 2015-3-16

@author: sWX231817
'''

class CreateVolBackResp(object):
    '''
    classdocs
    '''
    urn = None
    uri = None
    uuid = None
    taskUrn = None
    taskUri = None


    def __init__(self, _urn=None, _uri=None, _uuid=None, _taskUrn=None, _taskUri=None):
        '''
        Constructor
        '''
        self.urn = _urn
        self.uri = _uri
        self.uuid = _uuid
        self.taskUrn = _taskUrn
        self.taskUri = _taskUri
