'''
Created on 2015-3-16

@author: sWX231817
'''
class VmSnapshot(object):
    '''
    classdocs
    '''
    urn = None
    uri = None
    name = None
    description = None
    createTime = None
    type = None
    status = None
    childSnapshots = None


    def __init__(self, _urn=None, _uri=None, _name=None, _description=None, _createTime=None, _type=None, _status=None, _childSnapshots=None):
        '''
        Constructor
        '''
        self.urn = _urn
        self.uri = _uri
        self.name = _name
        self.description = _description
        self.createTime = _createTime
        self.type = _type
        self.status = _status
        self.childSnapshots = _childSnapshots
