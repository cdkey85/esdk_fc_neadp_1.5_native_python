'''
Created on 2015-3-16

@author: lWX232078
'''
from com.huawei.resources.common.AuthenticateResource import AuthenticateResource
from com.huawei.client.connection import RestClient
from com.huawei.resources.site.SiteResource import SiteResource
from com.huawei.client.log import *

if __name__ == '__main__':
    
    client = RestClient()
    client.connetToServer(host='172.22.4.4', port=7443, protocol='https')
    login = AuthenticateResource()
    aaa = login.login('fc01', 'Huawei@123');
#     LogInit(LogConf('../../log.conf','LOGCONF'))
     
    site = SiteResource()
    b = site.querySiteList()
#     b = login.logout()
    print b
    print b["errorCode"]
    print b["errorDes"]
    pass