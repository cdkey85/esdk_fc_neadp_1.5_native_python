# coding=utf-8
'''
Created on 2015-3-12

@author: sWX231817
'''

class SDKCommonResp(object):
    '''
    FC SDK 公共返回值。
    '''
    errorCode = None
    errorDes = None
    def __init__(self, _errorCode="00000000", _errorDes=''):
        '''
        Constructor
        '''
        self.errorCode = _errorCode
        self.errorDes = _errorDes
