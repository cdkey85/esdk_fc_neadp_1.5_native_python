'''
Created on 2015-3-7

@author: lWX232078
'''
from com.huawei.model.common.SDKCommonResp import SDKCommonResp

class LoginResp(SDKCommonResp):
    '''
    classdocs
    '''
    validity = None
    privilegeIds = None
    userId = None
    userName = None
    roleList = None
    rightType = None


    def __init__(self, _validity=None, _privilegeIds=None, _userId=None, _userName=None, _roleList=None, _rightType=None):
        '''
        Constructor
        '''
        self.validity = _validity
        self.privilegeIds = _privilegeIds
        self.userId = _userId
        self.userName = _userName
        self.roleList = _roleList
        self.rightType = _rightType
