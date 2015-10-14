'''
Created on 2015-3-16

@author: sWX231817
'''

class CreateVolBackReq(object):
    '''
    classdocs
    '''
    datastoreUrn = None
    name = None


    def __init__(self,_datastoreUrn=None,_name=None):
        '''
        Constructor
        '''
        self.datastoreUrn=_datastoreUrn
        self.name=_name  
