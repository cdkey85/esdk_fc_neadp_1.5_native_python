'''
Created on 2015-3-7

@author: lWX232078
'''

class FragmentLimen(object):
    '''
    classdocs
    '''
    fragmentTime = None
    limen = None


    def __init__(self, _fragmentTime = None,_limen = None):
        '''
        Constructor
        '''
        self.fragmentTime = _fragmentTime
        self.limen = _limen