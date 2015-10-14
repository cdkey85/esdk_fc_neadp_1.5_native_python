'''
Created on 2015-3-7

@author: sWX231817
'''

from com.huawei.model.vm.CPU import CPU
from com.huawei.model.vm.Memory import Memory


class VmRebootConfig(object):
    '''
    classdocs
    '''

    cpu = CPU()
    memory = Memory()


    def __init__(self, _cpu=None, _memory=None):
        '''
        Constructor
        '''
        self.cpu = _cpu
        self.memory = _memory
