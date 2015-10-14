#coding=utf-8
'''
Created on 2015-3-12

@author: lWX232078
'''
import logging  
import ConfigParser
import os

def ReadConf(confFile,sec):
    if not confFile:
        return None
    strpath = os.path.abspath(confFile)
    if not os.path.exists(strpath):
        raise Exception('%s is not exist'%(strpath))

    cf = ConfigParser.ConfigParser()
    cf.read(confFile)
    secs = cf.sections()
    if sec not in secs:
        raise Exception('%s is not in secs:%s'%(sec,str(secs)))

    items = cf.items(sec)
    idict = {}
    for e in items:
        idict[e[0]]=e[1]   
    return idict

class LogConf(object):
    '''
    classdocs
    '''
    LogFileDir = './'
    LogFileName  = 'log.log'
    LogFileSize = 0
    LogFileNumber = 0
    LogFileLevel = logging.NOTSET
    PrintLogToConsole = 0
    PrintLogLevel = 0
    
    def __init__(self,confFile=None,sec=None):
        '''
        Constructor
        '''
        self.ReadConfKey(confFile,sec)
        pass
    
    def ReadConfKey(self,confFile,sec):
        if confFile == None and sec == None:
            return None
         
        items = ReadConf(confFile,sec)
        #print items
        if 'logfiledir' in str(items.keys()):
            self.LogFileDir = items['logfiledir']
        if 'logfilename' in str(items.keys()):
            self.LogFileName = items['logfilename']
        if 'logfilesize' in str(items.keys()):
            self.LogFileSize = int(items['logfilesize'])
        if 'logfilenumber' in str(items.keys()):
            self.LogFileNumber = int(items['logfilenumber'])
        if 'logfilelevel' in str(items.keys()):
            logFileLevel = items['logfilelevel']
            self.LogFileLevel = self.getLogLevel(logFileLevel)
        if 'PrintLogToConsole'.lower() in str(items.keys()):
            self.PrintLogToConsole = int(items['PrintLogToConsole'.lower()])
        if('PrintLogLevel'.lower()) in str(items.keys()):
            printLogLevel = items['PrintLogLevel'.lower()]
            self.PrintLogLevel = self.getLogLevel(printLogLevel)
        pass   
    
    def getLogLevel(self,lev):
        idict = {'CRITICAL':logging.CRITICAL,'ERROR':logging.ERROR,'WARNING':logging.WARNING,'INFO':logging.INFO,'DEBUG':logging.DEBUG,'NOTSET':logging.NOTSET}
        if lev in idict.keys():
            return idict[lev]   
        pass
 
         
         
         