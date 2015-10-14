#coding=utf-8
'''
Created on 2015-3-7

@author: lWX232078
'''


class VolumeCreateParams(object):
    '''
    classdocs
    '''
    name = None
    quantityGB = None
    datastoreUrn = None
    uuid = None
    isThin = None
    type = None
    indepDisk = None
    persistentDisk = None
    volType = None


    def __init__(self,    
        _name = None,
        _quantityGB = None,
        _datastoreUrn = None,
        _uuid = None,
        _isThin = None,
        _type = None,
        _indepDisk = None,
        _persistentDisk = None,
        _volType = None):
        '''
        Constructor
        '''
        self.name = None
        self.quantityGB = None
        self.datastoreUrn = None
        self.uuid = None
        self.isThin = None
        self.type = None
        self.indepDisk = None
        self.persistentDisk = None
        self.volType = None