'''
Created on 2015-3-16

@author: sWX231817
'''
from com.huawei.model.vm.CurrentSnapshot import CurrentSnapshot
from com.huawei.model.vm.VmSnapshot import VmSnapshot

class ListVmSnapshotsResp(object):
    '''
    classdocs
    '''
    currentSnapshot = CurrentSnapshot()
    rootSnapshots = [VmSnapshot()]


    def __init__(self, _currentSnapshot=None, _rootSnapshots=None):
        '''
        Constructor
        '''
        self.currentSnapshot = _currentSnapshot
        self.rootSnapshots = _rootSnapshots
