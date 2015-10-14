'''
Created on 2015-3-6

@author: sWX231817
'''

class ListVmsReq(object):
    '''
    classdocs
    '''
    limit = None
    offset = None
    name = None    
    group = None
    scope = None
    isTemplate = None
    isLinkClone = None
    templateUrn = None
    status = None
    ip = None
    mac = None
    vmId = None
    uuid = None
    vmurns = [None]
    resourceGroupFlag = None
    detail = None
    description = None
    imcSetting = None
    isBindingHost = None
    vmType = None


    def __init__(self, _limit=None, _offset=None, _name=None, _group=None, _scope=None, _isTemplate=None, _isLinkClone=None,
                  _templateUrn=None, _status=None, _ip=None, _mac=None, _vmId=None, _uuid=None, _vmurns=None, 
                  _resourceGroupFlag=None, _detail=None, _description=None, _imcSetting=None, _isBindingHost=None, _vmType=None):
        '''
        Constructor
        '''
        self.limit = _limit
        self.offset = _offset
        self.name = _name    
        self.group = _group
        self.scope = _scope
        self.isTemplate = _isTemplate
        self.isLinkClone = _isLinkClone
        self.templateUrn = _templateUrn
        self.status = _status
        self.ip = _ip
        self.mac = _mac
        self.vmId = _vmId
        self.uuid = _uuid
        self.vmurns = _vmurns
        self.resourceGroupFlag = _resourceGroupFlag
        self.detail = _detail
        self.description = _description
        self.imcSetting = _imcSetting
        self.isBindingHost = _isBindingHost
        self.vmType = _vmType   
