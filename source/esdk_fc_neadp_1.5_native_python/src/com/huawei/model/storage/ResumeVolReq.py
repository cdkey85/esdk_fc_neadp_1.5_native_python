'''
Created on 2015-3-16

@author: sWX231817
'''

class ResumeVolReq(object):
    '''
    classdocs
    '''
    datastoreUrn = None
    isQuickResume = None


    def __init__(self, _datastoreUrn=None, _isQuickResume=None):
        '''
        Constructor
        '''
        self.datastoreUrn = _datastoreUrn
        self.isQuickResume = _isQuickResume
