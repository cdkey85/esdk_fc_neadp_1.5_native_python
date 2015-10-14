'''
Created on 2015-3-6

@author: sWX231817
'''

class CPU(object):
    '''
    classdocs
    '''
    quantity = None
    coresPerSocket = None
    reservation = None
    weight = None
    limit = None
    cpuHotPlug = None
    affinitySet = [None]


    def __init__(self, _quantity=None, _coresPerSocket=None, _reservation=None, _weight=None, _limit=None, _cpuHotPlug=None,
                  _affinitySet=None):
        '''
        Constructor
        '''
        self.quantity = _quantity
        self.coresPerSocket = _coresPerSocket
        self.reservation = _reservation
        self.weight = _weight
        self.limit = _limit
        self.cpuHotPlug = _cpuHotPlug
        self.affinitySet = _affinitySet
