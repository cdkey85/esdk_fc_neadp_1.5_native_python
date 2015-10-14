
import sys 
sys.path.append("..")

from com.huawei.resources.common.AuthenticateResource import AuthenticateResource
from com.huawei.client.connection import RestClient
from com.huawei.resources.net.PortGroupResource import PortGroupResource
from com.huawei.model.net.QueryPortGroupListReq import QueryPortGroupListReq
from com.huawei.resources.net.DVSwitchResource import DVSwitchResource
from com.huawei.client.log import *


if __name__ == '__main__':
    client = RestClient()
    client.connetToServer(host='172.22.4.4', port=7443, protocol='https')
    login = AuthenticateResource()
    aaa = login.login('fc01', 'Huawei@123');
    LogInit(LogConf('../../log.conf','LOGCONF'))
    
    net = PortGroupResource()
    
    b = net.queryPortGroup('/service/sites/4D9D0815/dvswitchs/1/portgroups/1')    
 
    
    print '----------------------------------------------------'
    req = QueryPortGroupListReq()
    req.limit = 100
    req.offset = 1

    b = net.queryPortGroupList('/service/sites/4D9D0815/dvswitchs/1', req)


    print '------------------------------------------------------'
    DV = DVSwitchResource()
    
    name = 'ManagementDVS'
    site_uri = '/service/sites/4D9D0815'
    b = DV.queryDVSwitchList(site_uri, location=None, name = name)
  
    login.logout()