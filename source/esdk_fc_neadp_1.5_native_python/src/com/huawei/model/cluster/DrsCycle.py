'''
Created on 2015-3-7

@author: lWX232078
'''

class DrsCycle(object):
    '''
    classdocs
    '''
    cycleType = None
    cycleSpec = None



    def __init__(self, _cycleType = None,_cycleSpec = None):
        '''
        Constructor
        '''
        
        self.cycleSpec = _cycleSpec
        self.cycleType = _cycleType