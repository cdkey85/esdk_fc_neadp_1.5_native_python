'''
Created on 2015-3-7

@author: lWX232078
'''

class ModifyVolumeReq(object):
    '''
    classdocs
    '''
    name = None
    indepDisk = None
    persistentDisk = None


    def __init__(self, _name = None,_indepDisk = None,_persistentDisk = None):
        '''
        Constructor
        '''
        self.name = _name
        self.indepDisk = _indepDisk
        self.persistentDisk = _persistentDisk