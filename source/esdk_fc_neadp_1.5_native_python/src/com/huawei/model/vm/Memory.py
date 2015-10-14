'''
Created on 2015-3-6

@author: sWX231817
'''

class Memory(object):
    '''
    classdocs
    '''
    quantityMB = None
    reservation = None
    weight = None
    limit = None
    memHotPlug = None


    def __init__(self, _quantityMB=None, _reservation=None, _weight=None, _limit=None, _memHotPlug=None):
        '''
        Constructor
        '''
        self.quantityMB = _quantityMB
        self.reservation = _reservation
        self.weight = _weight
        self.limit = _limit
        self.memHotPlug = _memHotPlug
