'''
Created on 2015-3-7

@author: lWX232078
'''

class DrsVmConfig(object):
    '''
    classdocs
    '''
    vmUrn = None
    behavior = None



    def __init__(self, _vmUrn=None,_behavior=None):
        '''
        Constructor
        '''
        self.vmUrn = _vmUrn
        self.behavior = _behavior