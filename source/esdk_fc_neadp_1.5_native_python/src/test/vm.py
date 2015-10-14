# coding=utf-8
'''
Created on 2015-3-7

@author: swx231817
'''

from com.huawei.client.connection import RestClient
from com.huawei.model.vm.AddNicReq import AddNicReq
from com.huawei.model.vm.AttachCdromReq import AttachCdromReq
from com.huawei.model.vm.AttachVolReq import AttachVolReq
from com.huawei.model.vm.CPU import CPU
from com.huawei.model.vm.GPU import GPU
from com.huawei.model.vm.CloneVmReq import CloneVmReq
from com.huawei.model.vm.CreateVmReq import CreateVmReq
from com.huawei.model.vm.CreateVmSnapshotReq import CreateVmSnapshotReq
from com.huawei.model.vm.VmCustomization import VmCustomization
from com.huawei.model.vm.DetachVolReq import DetachVolReq
from com.huawei.model.vm.Disk import Disk
from com.huawei.model.vm.ExportVmTempReq import ExportVmTempReq
from com.huawei.model.vm.ImportVmTempReq import ImportVmTempReq
from com.huawei.model.vm.ListVmsReq import ListVmsReq
from com.huawei.model.vm.Memory import Memory
from com.huawei.model.vm.ModifyNicReq import ModifyNicReq
from com.huawei.model.vm.OsOption import OsOption
from com.huawei.model.vm.StopVmReq import StopVmReq
from com.huawei.model.vm.RebootVmReq import RebootVmReq
from com.huawei.model.vm.UploadVmDataReq import UploadVmDataReq
from com.huawei.model.vm.VmConfig import VmConfig
from com.huawei.model.vm.Usb import Usb
from com.huawei.model.vm.UsbDevice import UsbDevice
from com.huawei.model.vm.Property import Property
from com.huawei.model.vm.Nic import Nic
from com.huawei.model.vm.NicSpecification import NicSpecification
from com.huawei.model.vm.Disk import Disk
from com.huawei.model.vm.DeleteVmReq import DeleteVmReq
from com.huawei.resources.common.AuthenticateResource import AuthenticateResource
from com.huawei.resources.vm.VmResource import VmResource
#from com.huawei.client.log import *
from com.huawei.client.utils import dict

def listOsInfos():
    bbb = resorce.listOsInfos("/service/sites/4D9D0815") 
    return bbb 
def deleteVm():
    req = DeleteVmReq()
    req.isFormat = 0
    bbb = resorce.deleteVm("/service/sites/4D9D0815/vms/i-000002E8", req) 
    return bbb 
def startVm():
    bbb = resorce.startVm("/service/sites/4D9D0815/vms/i-00000274") 
    return bbb 
def stopVm():
    req = StopVmReq()
    req.mode = 'force' 
    bbb = resorce.stopVm("/service/sites/4D9D0815/vms/i-00000274", dict(req))
    return bbb
def rebootVm():
    req = RebootVmReq()
    req.mode = 'force' 
    bbb = resorce.rebootVm("/service/sites/4D9D0815/vms/i-00000274", dict(req))
    return bbb
def queryVm():    
    bbb = resorce.queryVm("/service/sites/4D9D0815/vms/i-00000278") 
    return bbb
def listVms():
    req = ListVmsReq()
    req.limit = 5
    req.offset = 0
    req.scope="urn:sites:4D9D0815:volumes:1091"
    bbb = resorce.listVms("/service/sites/4D9D0815", dict(req))
    return bbb 
def addNic():  
    req = AddNicReq()
    req.portGroupUrn = 'urn:sites:4D9D0815:dvswitchs:1:portgroups:1'  
    bbb = resorce.addNic(vmUri="/service/sites/4D9D0815/vms/i-00000274", req=dict(req)) 
    return bbb
def attachCdrom():  
    req = AttachCdromReq()
    req.devicePath = "//172.24.0.232/Systems/Win_Pro_7_64.iso"
    bbb = resorce.attachCdrom(vmUri="/service/sites/4D9D0815/vms/i-00000286", req=dict(req)) 
    return bbb
def createVm():
    req = CreateVmReq()
    req.name = "createTest"
    req.location = "urn:sites:4D9D0815:clusters:79"
    req.group = "FC_test"
     
    opt = OsOption()
    opt.osType = "Linux"
    opt.osVersion = 99
    req.osOptions = dict(opt) 
     
    config = VmConfig()
    cpu = CPU()
    cpu.quantity = 1
    cpu.coresPerSocket = 1
    config.cpu = dict(cpu)
    mem = Memory()
    mem.quantityMB = 128
    config.memory = dict(mem)
    
    disk1 = Disk()
    disk1.datastoreUrn = "urn:sites:4D9D0815:datastores:1"
    disk1.sequenceNum = 2
    disk1.quantityGB = 1
    disk1.type = "share"
    disk2 = Disk()
    disk2.datastoreUrn = "urn:sites:4D9D0815:datastores:1"
    disk2.sequenceNum = 3
    disk2.quantityGB = 1
    disk2.type = "share"
    config.disks = [dict(disk1), dict(disk2)]
    
    req.vmConfig = dict(config) 
     
    bbb = resorce.createVm("/service/sites/4D9D0815", dict(req))
    return bbb
def delNic():    
    bbb = resorce.delNic("/service/sites/4D9D0815/vms/i-00000274/nics/3") 
    return bbb
def modifyNic():
    nicUri = "/service/sites/4D9D0815/vms/i-00000272/nics/10"
    req = ModifyNicReq()
    req.mac = "28:6e:d4:88:c8:e4"
    req.name = "Nic1_Modify2"
    req.portGroupUrn = "urn:sites:4D9D0815:dvswitchs:1:portgroups:2"
    bbb = resorce.modifyNic(nicUri, req.__dict__) 
    return bbb
def attachVol():
    req = AttachVolReq()
    req.volUrn = "urn:sites:4D9D0815:volumes:926"
    bbb = resorce.attachVol("/service/sites/4D9D0815/vms/i-00000274", dict(req)) 
    return bbb
def detachVol():
    req = DetachVolReq()
    req.volUrn = "urn:sites:4D9D0815:volumes:926"
    bbb = resorce.detachVol("/service/sites/4D9D0815/vms/i-00000274", dict(req)) 
    return bbb
def attachTools():
    bbb = resorce.attachTools("/service/sites/4D9D0815/vms/i-00000251") 
    return bbb
def detachTools():
    bbb = resorce.detachTools("/service/sites/4D9D0815/vms/i-00000251") 
    return bbb

def uploadData():
    req = UploadVmDataReq()
    req.fileName = "/home/temp/terst.txt"
    req.vmData = "test"
    bbb = resorce.uploadData("/service/sites/4D9D0815/vms/i-00000251", dict(req))
    return bbb
def createVmSnapshot():
    req = CreateVmSnapshotReq()
    req.name = "test"
    bbb = resorce.createVmSnapshot("/service/sites/4D9D0815/vms/i-00000274", dict(req))
    return bbb
def listVmSnapshots():
    bbb = resorce.listVmSnapshots("/service/sites/4D9D0815/vms/i-0000026E")
    return bbb
def queryVmSnapshot():
    bbb = resorce.queryVmSnapshot("/service/sites/4D9D0815/vms/i-00000274/snapshots/3820")
    return bbb
def deleteVmSnapshot():
    bbb = resorce.deleteVmSnapshot("/service/sites/4D9D0815/vms/i-00000274/snapshots/3820")
    return bbb
def exportVm():
    req = ExportVmTempReq()
    req.name = "zxc"
    req.format = "ovf"
    req.username = "CHINA\\admin"
    req.password = "Huawei@123"
    req.isOverwrite = True
    req.url = "//172.24.0.232/Share/zxc"
    req.protocol = "cifs"

    config = VmConfig()
    cpu = CPU()
    cpu.quantity = 1
    cpu.coresPerSocket = 1
    cpu.cpuHotPlug = 0
    cpu.limit = 0
    cpu.weight = 1000;
    config.cpu = dict(cpu)
    
    mem = Memory()
    mem.quantityMB = 128
    mem.reservation = 0
    mem.weight = 1280
    config.memory = dict(mem)
    
    pp = Property();
    pp.isAutoUpgrade = True;
    pp.isEnableMemVol = True;
    pp.isEnableHa = False;
    pp.vmFaultProcess = "notprocess";
    pp.attachType = False;
    pp.clockMode = "freeClock";
    config.properties = dict(pp)
    
    di = Disk()
    di.quantityGB = 1
    di.sequenceNum = 1
    di.datastoreUrn = "urn:sites:4D9D0815:datastores:1"
    di.isDataCopy = True
    di.volType = 0
    config.disks = [dict(di)]
    
    nic = Nic();
    nic.sequenceNum = 1;
    nic.portGroupUrn = "urn:sites:4D9D0815:dvswitchs:1:portgroups:1";
    nic.virtIo = 0;
    config.nics = [dict(nic)]
    
    gpu = GPU()
    gpu.gpuUrn = "SDGSDGSDG"
    config.gpu = [dict(gpu)]

    usb = Usb();
    usbDevice = UsbDevice(); 
    usbDevice .usbUrn = [dict(usb)]
    config.usb = [dict(usb)]
    req.vmConfig = dict(config)
    bbb = resorce.exportVm("/service/sites/4D9D0815/vms/i-00000278", dict(req))
    return bbb
def importVm():
    req = ImportVmTempReq()
    req.name = "impor"
    req.location = "urn:sites:4D9D0815:clusters:79"
     
    opt = OsOption()
    opt.osType = "Linux"
    opt.osVersion = 99
    req.osOptions = dict(opt) 
     
    config = VmConfig()
    cpu = CPU()
    cpu.quantity = 1
    cpu.coresPerSocket = 1
    config.cpu = dict(cpu)
    mem = Memory()
    mem.quantityMB = 128
    config.memory = dict(mem)
    di = Disk()
    di.quantityGB = 1
    di.sequenceNum = 1
    di.datastoreUrn = "urn:sites:4D9D0815:datastores:1"
    di.isDataCopy = True
    di.volType = 0
    config.disks = [dict(di)]
    req.vmConfig = dict(config)
    req.url = "//1.1.1.1/z/x.ova"
    req.protocol = "cifs"
    
    req.autoBoot = False 
    bbb = resorce.importVm("/service/sites/4D9D0815", dict(req))
    return bbb
def cloneVm():
    req = CloneVmReq()
    req.name = "ccc";  # 【可选】虚拟机别名，长度[0,256]。
#     req.location = "urn:sites:4D9D0815:clusters:79";
#     req.autoBoot = False;  # 【可选】是否自动启动，默认启动：true。 
#     req.description = "克隆虚拟机dsagsdgsdgsdgsdg";  # 【可选】虚拟机描述信息，长度[0，1024]。 
#     req.group = None;  # 【可选】虚拟机组名称，长度为[0，1024]. 
#     req.isBindingHost = False;  # 【可选】是否与主机绑定； true：与主机绑定， false：不绑定主机； 注：当location为hostUrn时有效； 若指定主机不位于集群下时系统自动将此属性处理为true，若主机位于集群下时默认为false。 
#     req.isMultiDiskSpeedup = False;  # 【可选】是否开启磁盘加速，默认false。 
#     req.uuid = None;  # UUID，虚拟机唯一标识，创建占位虚拟机时必选，其他情况下可选,【可选】虚拟机UUID，精确匹配查询。 。 
#     req.isLinkClone = False;  # 【可选】是否为链接克隆虚拟机。
#     req.fileMode = True  # 【可选】是否为file模式（预留字段，不建议填写）。 
#     req.fileName = "KKKKKKKK"  # 【可选】自定义数据存放的文件名，长度[1,64]。 
#     req.publickey = "sgsdgsdgsdgsdgsdg";  # 【可选】虚拟机密钥的公钥字符串，只支持linux操作系统。 
#     req.regionInfo = None;  # 【可选】ID盘信息；isLinkClone为true时才需设置，如果不设置当做空字符串处理；长度需在[0,1024]内。 
#     
#     vmc = VmCustomization();
#     vmc.description = None;
#     vmc.domain = None; 
#     vmc.domainName = None;
#     vmc.domainPassword = None;
#     vmc.hostname = "CNA01";
#     vmc.name = "hgfhfhgfghfh";
# #     nicSpecification = NicSpecification();
# #     nicSpecification.adddns = "123.23.232.25";
# #     nicSpecification.adddns6 = "fe80::5c71:d164:4ddb:c962%13";
# #     nicSpecification.autoConfEnabled6 = False;
# #     nicSpecification.dhcpEnabled6 = False;
# #     #nicSpecification.gateway = "123.23.232.0";
# #     nicSpecification.gatewayIpAddr6 = "123.233.232.323";
# #     nicSpecification.ip = "12.12.25.25";
# #     nicSpecification.ipVersion = 8;
# #    # nicSpecification.netmask = "12.12.125.1";
# #     nicSpecification.sequenceNum = 11;
# #     nicSpecification.setdns = "123.23.232.25";#地址表示：123.23.232.25
# #     nicSpecification.setdns6 = "fe80::5c71:d164:4ddb:c962%13";#地址表示采用16位，类似fe80::5c71:d164:4ddb:c962%13
#     vmc.osType = "Windows";
#     vmc.ouName = "sdgsdgsdg";
#     vmc.password = None;
#     vmc.workgroup = "jhhg";
#    # vmc.nicSpecification = [dict(nicSpecification)]
#     req.vmCustomization = dict(vmc)
#     
# #     #VNC信息--VncAccessInfo对象
# #     vnc = VncAcessInfo(); #vnc访问控制信息
# #     vnc.hostIp = "110.168.20.3";#虚拟机所在主机IP地址，null为非法值，其他为合法值，仅在查询时有效。 
# #     vnc.vncPassword = "44444d";#必填字段，虚拟机VNC密码，当修改VNC密码时，密码最大长度不超过8个字符，仅支持英文大小写字母和数字。  
# #     vnc.vncPort = 7443;#虚拟机VNC端口，-1为非法值，其他为合法值，仅在查询时有效。 
# #     req.vncAcessInfo = dict(vnc) 
# 
#     # 操作系统信息--OsOption对象
#     opt = OsOption()  # 客户操作系统信息
#     opt.osType = "Windows";  # 虚拟机操作系统类型，值：Windows，Linux，Other； 创建虚拟机时必选，修改时可选。 
#     opt.osVersion = 201;  # 操作系统版本号，创建虚拟机时必选。 
#     opt.guestOSName = "";  # 【可选】guest OS名称，长度[0,64]； 在OS version为 201-其他Windows(32 bit)、202-其他Windows(64 bit)、301-其他Linux(32 bit)、302-其他Linux(64 bit)、401-其他(32 bit)、402-其他(64 bit)时生效。 
#     req.osOptions = dict(opt) 
#     
#     # 虚拟机配置信息--VmConfig对象
#     config = VmConfig();  # 虚拟机配置信息
#     cpu = CPU();  # CPU规格
#     cpu.limit = 1000;  # 【可选】虚拟机cpu上限，单位是MHz，0（默认）代表不限制。 大小不能超过虚拟机quantity*站点下主机的最大CPU主频 。 
#     cpu.coresPerSocket = 1;  # 每CPU插槽的CPU核数，要求能够整除虚拟机的总核数，对于不同的操作系统，所支持的最大核数不同。  
#     cpu.quantity = 1;  # 虚拟机的总核数，范围[1，64]，对于不同的操作系统，所支持的最大核数不同。 
#     cpu.reservation = 0;  # 虚拟机CPU的预留值，单位为MHz，0（默认）代表不预留。 大小不能超过虚拟机quantity*站点下主机的最大CPU主频 。 
#     cpu.weight = 2000;  # 虚拟机cpu的份额，无单位，范围[1, 128000]，默认quantity*1000。 
#     config.cpu = dict(cpu)
#     
#     memory = Memory();  # 内存规格 
#     memory.quantityMB = 1024;  # 虚拟机内存总大小(单位m)，128~1024*1024。 
#     memory.weight = 10240;  # 【可选】虚拟机内存的份额，个数，无单位，范围[1, 1024*1024*20]，默认quantity*10。 
#     memory.reservation = 0;  # 【可选】虚拟机内存的预留值，单位为m，默认0，0代表不预留，大小不能超过虚拟机内存大小。 
#     config.memory = dict(memory)
# 
#     properties = Property();  # 虚拟机属性
#     properties.secureVmType = "";  # 虚拟机安全策略： SVM 安全服务虚拟机; GVM 安全用户虚拟机; 注：当该字段填写时，内存预留默认等于虚拟机内存，输入值无效。 
#     properties.vmFaultProcess = "notprocess";  # 虚拟机蓝屏处理策略：不处理(notprocess)，ha(ha)或重启(reboot)。 
#     properties.attachType = True;  # 【可选】块设备的挂卷方式，是否支持基本共享存储向存储虚拟化热迁移，false：不支持（默认），true：支持。 
#     properties.bootOption = "disk";  # 【可选】虚拟机第一启动选项，包括网络(pxe)，硬盘(disk)和光驱(cdrom)启动方式，默认disk; 说明：（1）创建空虚拟机时请选择光驱启动，创建PVS虚拟机时请选择网络启动； （2）若第一启动项为网络、光驱时系统自动设置第二启动项为硬盘。 
#     properties.gpuShareType = "normal";  # 【可选】GPU共享类型：server，client，normal（默认）。 
#     properties.isAutoUpgrade = False;  # 【可选】PV driver是否自动化升级，true：自动升级（默认），false:手动升级。 
#     properties.isEnableMemVol = False;  # 【可选】是否有内存卷，默认为true。 
#     properties.isEnableHa = True;  # 【可选】虚拟机是否支持HA，默认true。 
#     properties.isReserveResource = True;  # 是否始终保留资源，仅在绑定主机时生效；true 保留，false 不保留（默认）。 
#     properties.reoverByHost = True;  # 【可选】主机上电后是否随主机同时启动，默认为false，对于可靠性要求高的虚拟机推荐设置为true。 
#     properties.clockMode = "freeClock";  # 【可选】虚拟机的时钟模式，包括自由时(freeClock)钟和同步时钟(synchClock)，默认自由时钟。 
#     config.properties = dict(properties) 
# 
#     disk = Disk();  # 虚拟机磁盘规格
#     disk.datastoreUrn = "urn:sites:4D9D0815:datastores:1";  # 存储URI地址。 
#     disk.diskName = "disk006";  # 【可选】卷名称，长度[0,256]，可以重复. 如果请求中无name，或者name为””，则会自动生成name。 
#     disk.indepDisk = False;  # 【可选】是否独立磁盘，不携带时表示否：false，表示磁盘受快照影响。 
#     disk.isThin = False;  # 【可选】是否精简制备；在volumeUrn不携带时，生效，默认false。 
#     disk.maxReadBytes = 24;  # 每秒最大读字节数，单位为KB/s。 
#     disk.maxReadRequest = 343;  # 每秒最大读请求个数，单位为个/s。 
#     disk.maxWriteBytes = 23;  # 每秒最大写字节数，单位为KB/s
#     disk.maxWriteRequest = 2;  # 每秒最大写请求个数，单位为个/s。 
#     disk.pciType = "IDE";  # 【可选】磁盘挂载的总线类型，55555当前版本为：“IDE”（默认），“SCSI”； 只有在裸设备映射上创建的磁盘才可以挂载到SCSI总线上，其它的都是IDE总线上。 如果是以前版本，都是默认IDE。 
#     disk.persistentDisk = True;  # 【可选】是否持久化磁盘，不携带时表示为是(true)，表示卷为持久化磁盘。 
#     disk.quantityGB = 1;  # 虚拟机磁盘大小，单位：GB；系统卷大小不超过2T
#     disk.sequenceNum = 1;  # 磁盘对应的总线槽位编号，每种总线类型的编号分别为1-23。必选。不可与现有同一总线类型的重复
#     disk.volType = 0;  # 【可选】磁盘类型参数，支持创建、查询虚拟机接口，取值为： 0：普通卷（默认）; 1：延迟置零卷. 注：该字段在isThin参数为false时生效，在isthin参数为true时失效。 
#     disk.type = "share";  # 卷类型，注册虚拟机（必选）、查询虚拟机使用，取值为normal（普通卷）、share（共享卷）。 
#     # disk.volumeUrn = "urn:sites:4D9D0815:volumes:347";#硬盘对应卷标识，表示使用已有的卷，此时忽略后面的参数； 创建虚拟机、模板部署虚拟机、虚拟机克隆为模板、模板克隆为模板时，可选； 查询虚拟机响应中系统会返回此参数。 
#     disk.volumeUuid = "";  # 注册虚拟机时必选，其他情况可选。 
#     config.disks = [dict(disk)]
# 
#     nic = Nic();  # 虚拟机网卡信息
#     nic.ip = "10.123.20.23";  # IP地址，系统内部分配或从虚拟机内部获取的IP。 添加网卡、创建虚拟机时入参不携带，查询网卡或虚拟机信息中携带的网卡信息中携带。
#     nic.mac = "28:6e:d4:88:b4:f3";  # Mac地址，系统系统内部分配。 添加网卡，创建虚拟机，模板部署虚拟机，虚拟机克隆为虚拟机，模板克隆为模板，虚拟机克隆为虚拟机模板时入参不携带时由系统自动分派。 查询网卡或虚拟机信息中携带的网卡信息中携带。 
#     nic.name = "sgdsgsdg";  # 【可选】虚拟机网卡名称。 注：当模板部署/克隆虚拟机，虚拟机克隆为模板/虚拟机时此参数需要与原虚拟机/模板的网卡名相同。 
#     nic.nicType = 1;  # 网卡类型：1：inic网卡，其他：普通网卡，仅在查询时有效。 
#     nic.portGroupName = "managePortgroup55555";  # 【可选】portGroup名称。 
#     nic.portGroupUrn = "urn:sites:4D9D0815:dvswitchs:1:portgroups:1";  # 必填，portGroup标识，创建网卡时必选，修改网卡时可选。 
#     nic.virtIo = 0;  # 【可选】网卡类型，0: HW_X_NET (默认值)；1: HW_V_NET；不携带使用默认值。
#     config.nics = [dict(nic)]
# 
#     req.vmConfig = dict(config)  
#     req.isTemplate = True
#     
#     # req.vmDatas = [dict(nicSpecification)]
#     # req.vmDatas = ""#【可选】虚拟机自定义数据列表，fileNames有值时生效。 
    bbb = resorce.cloneVm("/service/sites/4D9D0815/vms/i-000002E6", dict(req))

#     bbb = resorce.cloneVm("/service/sites/4D9D0815/vms/i-0000028C", dict(req))
    return bbb


if __name__ == '__main__':
    client = RestClient()
    client.connetToServer(host='172.22.4.4', port=7443, protocol='https')
    login = AuthenticateResource()
    aaa = login.login('fc01', 'Huawei@123');
    
#    LogInit(LogConf("../../log.conf", "LOGCONF"))
    resorce = VmResource()
    
    exportVm()
