'''
Created on 2015-3-6

@author: lWX232078
'''

class DrsExtensionConfig(object):
    '''
    classdocs
    '''
    key = None
    value = None


    def __init__(self,_key = None,_value = None):
        '''
        Constructor
        '''
        self.key = _key
        self.value = _value