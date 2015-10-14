'''
Created on 2015-3-16

@author: sWX231817
'''

class CurrentSnapshot(object):
    '''
    classdocs
    '''
    urn = None
    uri = None
    name = None


    def __init__(self, _urn=None, _uri=None, _name=None):
        '''
        Constructor
        '''
        self.urn = _urn
        self.uri = _uri
        self.name = _name
