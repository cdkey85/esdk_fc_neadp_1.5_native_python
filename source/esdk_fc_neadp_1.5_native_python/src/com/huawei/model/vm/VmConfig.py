'''
Created on 2015-3-4

@author: sWX231817
'''

from com.huawei.model.vm.CPU import CPU
from com.huawei.model.vm.Memory import Memory
from com.huawei.model.vm.Disk import Disk
from com.huawei.model.vm.Nic import Nic
from com.huawei.model.vm.Usb import Usb
from com.huawei.model.vm.GPU import GPU
from com.huawei.model.vm.Property import Property

class VmConfig(object):
    '''
    classdocs
    '''
    cpu = CPU()
    memory = Memory()
    disks = [Disk()]
    nics = [Nic()]
    usb = [Usb()]
    gpu = [GPU()]
    properties = [Property()]


    def __init__(self, _cpu=None, _memory=None, _disks=None, _nics=None, _usb=None, _gpu=None, _properties=None):
        '''
        Constructor
        '''
        self.cpu = _cpu
        self.memory = _memory
        self.disks = _disks
        self.nics = _nics
        self.usb = _usb
        self.gpu = _gpu
        self.properties = _properties