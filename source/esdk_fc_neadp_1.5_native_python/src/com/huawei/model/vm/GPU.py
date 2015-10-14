'''
Created on 2015-3-6

@author: sWX231817
'''

class GPU(object):
    '''
    classdocs
    '''
    gpuUrn = None 
    isEffected = None


    def __init__(self, _gpuUrn=None, _isEffected=None):
        '''
        Constructor
        '''
        self.gpuUrn = _gpuUrn 
        self.isEffected = _isEffected
        
