'''
Created on 2015-3-9

@author: lWX232078
'''

class RemoveVolumeResp(object):
    '''
    classdocs
    '''
    taskUrn=None
    taskUri=None


    def __init__(self,_taskUrn=None,_taskUri=None):
        '''
        Constructor
        '''
        self.taskUri = _taskUri
        self.taskUrn = _taskUrn