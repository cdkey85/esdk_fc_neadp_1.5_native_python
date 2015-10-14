'''
Created on 2015-3-6

@author: sWX231817
'''

class CreateVmSnapshotReq(object):
    '''
    classdocs
    '''
    name = None
    description = None
    needMemoryShot = None
    isConsistent = None
    type = None


    def __init__(self, _name=None, _description=None, _needMemoryShot=None, _isConsistent=None, _type=None):
        '''
        Constructor
        '''
        self.name = _name
        self.description = _description
        self.needMemoryShot = _needMemoryShot
        self.isConsistent = _isConsistent
        self.type = _type
