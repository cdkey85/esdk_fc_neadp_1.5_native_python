'''
Created on 2015-3-13

@author: sWX231817
'''

from com.huawei.model.vm.OsInfo import OsInfo
from com.huawei.model.common.SDKCommonResp import SDKCommonResp

class ListOsInfosResp(SDKCommonResp):
    '''
    classdocs
    '''
    windows = [OsInfo()]
    linux = [OsInfo()]
    other = [OsInfo()]


    def __init__(self, _windows=None, _linux=None, _other=None):
        '''
        Constructor
        '''
        self.windows = _windows
        self.linux = _linux
        self.other = _other
