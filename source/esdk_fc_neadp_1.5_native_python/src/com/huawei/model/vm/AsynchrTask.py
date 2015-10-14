'''
Created on 2015-3-7

@author: sWX231817
'''

class AsynchrTask(object):
    '''
    classdocs
    '''
    taskUrn = None
    taskUri = None

    def __init__(self, _taskUrn=None, _taskUri=None):
        '''
        Constructor
        '''
        self.taskUrn = _taskUrn
        self.askUri = _taskUri
