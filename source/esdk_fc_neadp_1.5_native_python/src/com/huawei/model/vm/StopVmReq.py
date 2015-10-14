'''
Created on 2015-3-4

@author: sWX231817
'''

class StopVmReq(object):
    '''
    classdocs
    '''
    mode = None

    def __init__(self, _mode=None):
        '''
        Constructor
        '''
        self.mode = _mode
