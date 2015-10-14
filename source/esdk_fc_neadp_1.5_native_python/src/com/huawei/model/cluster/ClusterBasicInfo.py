'''
Created on 2015-3-7

@author: lWX232078
'''
import CpuResource
import MemoryResource

class ClusterBasicInfo(object):
    '''
    classdocs
    '''
    urn = None
    uri = None
    name = None
    parentObjUrn = None
    parentObjName = None
    description = None
    cpuResource = None
    memResource = None
    tag = None


    def __init__(self,_urn = None,
    _uri = None,
    _name = None,
    _parentObjUrn = None,
    _parentObjName = None,
    _description = None,
    _cpuResource = None,
    _memResource = None,
    _tag = None ):
        '''
        Constructor
        '''
        self.urn = None
        self.uri = None
        self.name = None
        self.parentObjUrn = None
        self.parentObjName = None
        self.description = None
        self.cpuResource = None
        self.memResource = None
        self.tag = None