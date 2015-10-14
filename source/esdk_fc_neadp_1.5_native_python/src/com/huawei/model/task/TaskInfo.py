'''
Created on 2015-3-7

@author: lWX232078
'''

class TaskInfo(object):
    '''
    classdocs
    '''
    urn = None
    uri = None
    type = None
    entityUrn = None
    entityName = None
    startTime = None
    finishTime = None
    user = None
    status = None
    progress = None
    reason = None
    reasonDes  = None
    cancelable = None
    cancelled = None



    def __init__(self,    
        _urn = None,
        _uri = None,
        _type = None,
        _entityUrn = None,
        _entityName = None,
        _startTime = None,
        _finishTime = None,
        _user = None,
        _status = None,
        _progress = None,
        _reason = None,
        _reasonDes  = None,
        _cancelable = None,
        _cancelled = None):
        '''
        Constructor
        '''
        self.urn = _urn
        self.uri = _uri
        self.type = _type
        self.entityUrn = _entityUrn
        self.entityName = _entityName
        self.startTime = _startTime
        self.finishTime = _finishTime
        self.user = _user
        self.status = _status
        self.progress = _progress
        self.reason = _reason
        self.reasonDes  = _reasonDes
        self.cancelable = _cancelable
        self.cancelled = _cancelled