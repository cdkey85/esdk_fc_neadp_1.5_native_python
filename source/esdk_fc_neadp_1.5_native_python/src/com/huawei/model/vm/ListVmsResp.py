'''
Created on 2015-3-6

@author: sWX231817
'''

from com.huawei.model.vm.VmInfo import VmInfo

class ListVmsResp(object):
    '''
    classdocs
    '''
    total = None
    vms = [VmInfo()]

    def __init__(self, _total=None, _vms=None):
        '''
        Constructor
        '''
        self.total = _total
        self.vms = _vms
