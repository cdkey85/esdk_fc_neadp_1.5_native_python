#coding=utf-8

'''
Created on 2015-3-12

@author: lWX232078
'''

import platform
import os
import sys
import logging  
import logging.handlers 
#from ReadConfig import ReadConfig
from com.huawei.client.readConfig import LogConf

CRITICAL = logging.CRITICAL
ERROR = logging.ERROR
WARNING = logging.WARNING
INFO = logging.INFO
DEBUG = logging.DEBUG
NOTSET = logging.NOTSET


LOGMODE = 'MYLOGGER'
logger = None

def LogInit(logCog = LogConf()): 
    if not logCog:
        raise Exception('log config is None')
    
    global logger
    # 创建一个logger
    logger = logging.getLogger(LOGMODE)
    logger.setLevel(logging.DEBUG)
  
    #创建日志路劲
    if not os.path.exists(logCog.LogFileDir):
        os.makedirs(logCog.LogFileDir, 0755)
        pass
    
    
    # 创建一个handler，用于写入日志文件
    #strpath = os.path.abspath(logCog.LogFileDir)
    if platform.system() == 'Windows':
        logfilepath=logCog.LogFileDir + '\\' +logCog.LogFileName
        pass
    else:
        logfilepath=logCog.LogFileDir + '/' +logCog.LogFileName
        pass
        
    # 创建一个handler，用于写入日志文件
    fh = logging.handlers.RotatingFileHandler(logfilepath, maxBytes = 1024*1024*logCog.LogFileSize, backupCount = logCog.LogFileNumber)
    fh.setLevel(logCog.LogFileLevel)
    
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s]%(message)s')
    fh.setFormatter(formatter)
    
    # 给logger添加handler
    logger.addHandler(fh)
    if logCog.PrintLogToConsole == 1: 
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logCog.PrintLogLevel)
    
        # 定义handler的输出格式
        ch.setFormatter(formatter)
       
        # 给logger添加handler
        logger.addHandler(ch)
        pass
    
    logger.critical('------------------log start---------------------------') 

       
def LOG(level,msg,*args,**kwargs):
    
    logger = logging.getLogger(LOGMODE)
    funcname  = sys._getframe().f_back.f_code.co_name
    line = sys._getframe().f_back.f_lineno 
    #Msg = '[%(name)s,%(lineno)d] :'%{'name':funcname,'lineno':line} 
    #Msg += msg
    #msg =Msg
    
    if(level == CRITICAL):
        logger.critical(msg,*args,**kwargs)
        pass
    if(level == ERROR):
        logger.error(msg,*args,**kwargs)
        pass
    if(level == WARNING):   
        logger.warning(msg,*args,**kwargs)
        pass
    if(level == INFO):
        logger.info(msg,*args,**kwargs)
        pass
    if(level == DEBUG):
        logger.debug(msg,*args,**kwargs)
        pass
    if(level == NOTSET):
        logger.notset(msg,*args,**kwargs)
        pass
      
     

            