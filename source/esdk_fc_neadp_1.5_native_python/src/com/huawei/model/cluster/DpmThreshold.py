'''
Created on 2015-3-7

@author: lWX232078
'''

class DpmThreshold(object):
    '''
    classdocs
    '''
    cpu = None
    memory = None


    def __init__(self, _cpu = None,_memory =None):
        '''
        Constructor
        '''
        self.cpu = _cpu
        self.memory = _memory