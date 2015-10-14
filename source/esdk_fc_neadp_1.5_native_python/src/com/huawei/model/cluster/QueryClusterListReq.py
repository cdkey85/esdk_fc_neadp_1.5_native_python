'''
Created on 2015-3-9

@author: lWX232078
'''

class QueryClusterListReq(object):
    '''
    classdocs
    '''
    tag = None
    name = None
    parentObjUrn = None
    clusterUrns = [None]


    def __init__(self,_tag=None,_name=None,_parentObjUrn = None,_clusterUrns = None ):
        '''
        Constructor
        '''
        self.tag = _tag
        self.name = _name
        self.parentObjUrn = _parentObjUrn
        self.clusterUrns = _clusterUrns