# coding=utf-8
'''
Created on 2015-3-6

@author: sWX231817
'''

import urllib

from com.huawei.client.connection import RestClient
from com.huawei.model.vm.AddNicReq import AddNicReq
from com.huawei.model.vm.AsynchrTask import AsynchrTask
from com.huawei.model.vm.AttachCdromReq import AttachCdromReq
from com.huawei.model.vm.AttachVolReq import AttachVolReq
from com.huawei.model.vm.CloneVmReq import CloneVmReq
from com.huawei.model.vm.CreateVmReq import CreateVmReq
from com.huawei.model.vm.CreateVmSnapshotReq import CreateVmSnapshotReq
from com.huawei.model.vm.DetachVolReq import DetachVolReq
from com.huawei.model.vm.ExportVmTempReq import ExportVmTempReq
from com.huawei.model.vm.ImportVmTempReq import ImportVmTempReq
from com.huawei.model.vm.ListVmsReq import ListVmsReq
from com.huawei.model.vm.ListVmsResp import ListVmsResp
from com.huawei.model.vm.ModifyNicReq import ModifyNicReq
from com.huawei.model.vm.QueryVmSnapshotResp import QueryVmSnapshotResp
from com.huawei.model.vm.ListVmSnapshotsResp import ListVmSnapshotsResp
from com.huawei.model.vm.StopVmReq import StopVmReq
from com.huawei.model.vm.RebootVmReq import RebootVmReq
from com.huawei.model.vm.UploadVmDataReq import UploadVmDataReq
from com.huawei.model.vm.VmInfo import VmInfo
from com.huawei.model.vm.VmTaskResp import VmTaskResp

from com.huawei.model.vm.DeleteVmReq import DeleteVmReq
from com.huawei.model.vm.ListOsInfosResp import ListOsInfosResp
from com.huawei.client.utils import dict


class VmResource(object):
    '''
    classdocs
    '''
    global client
    client = RestClient()

    def __init__(self):
        '''
        Constructor
        '''
        pass
        
    def createVm(self, siteUri, req=CreateVmReq()):
        '''
        function:创建虚拟机
        '''
        response = client.send(method='POST', url=siteUri + "/vms", body=dict(req), resp=VmTaskResp(), name="createVm")
        return response 
    
    def deleteVm(self, vmUri, req=DeleteVmReq()):
        '''
        function:删除虚拟机
        '''
        url = vmUri
        reqEx = dict(req)
        if reqEx:
            url += "?" + urllib.urlencode(reqEx).replace("%5B", "").replace("%3A", ":").replace("%27", "").replace("%5D", "").replace("+", "")
        response = client.send(method='DELETE', url=url, body=None, resp=VmTaskResp(), name="deleteVm")
        return response 

    def uploadData(self, vmUri, req=UploadVmDataReq()):
        '''
        function:给虚拟机传入自定义数据
        '''
        response = client.send(method='POST', url=vmUri + "/action/uploadVmData", body=dict(req), resp=AsynchrTask(), name="uploadData")
        return response

    def startVm(self, vmUri, req=None):
        '''
        function:启动/唤醒虚拟机
        '''
        response = client.send(method='POST', url=vmUri + "/action/start", body=None, resp=AsynchrTask(), name="startVm")
        return response 
    
    def stopVm(self, vmUri, req=StopVmReq()):
        '''
        function:停止虚拟机
        '''
        response = client.send(method='POST', url=vmUri + "/action/stop", body=dict(req), resp=AsynchrTask(), name="stopVm")
        return response 
    
    def rebootVm(self, vmUri, req=RebootVmReq()):
        '''
        function:重启虚拟机
        '''
        response = client.send(method='POST', url=vmUri + "/action/reboot", body=dict(req), resp=AsynchrTask(), name="rebootVm")
        return response 
    
    def queryVm(self, vmUri):
        '''
        function:查询指定虚拟机信息
        '''
        response = client.send(method='GET', url=vmUri, body=None, resp=VmInfo(), name="queryVm")
        return response 
    
    def listVms(self, siteUri, req=ListVmsReq()):
        '''
        function:过滤分页查询所有虚拟机信息
        '''
        url = siteUri + "/vms"
        reqEx = dict(req)
        if reqEx:
            url += "?" + urllib.urlencode(reqEx).replace("%5B", "").replace("%3A", ":").replace("%27", "").replace("%2C+", "&vmurns=").replace("%5D", "").replace("+", "")
        response = client.send(method='GET', url=url, body=None, resp=None, name="listVms")
        return response     
    
    def attachCdrom(self, vmUri, req=AttachCdromReq()):
        '''
        function:挂载光驱
        '''
        response = client.send(method='POST', url=vmUri + "/action/attachCdrom", body=dict(req), resp=AsynchrTask(), name="attachCdrom")
        return response 
    
    def addNic(self, vmUri, req=AddNicReq()):
        '''
        function:添加网卡
        '''
        response = client.send(method='POST', url=vmUri + "/virtualNics", body=dict(req), resp=VmTaskResp(), name="addNic")
        return response    
    
    def delNic(self, nicUri):
        '''
        function:删除网卡
        '''
        vmUri = nicUri[:(nicUri.find("nic") - 1)]
        nicId = nicUri[(nicUri.find("nic") - len(nicUri) + 5):]
        response = client.send(method='DELETE', url=vmUri + "/virtualNics/" + nicId, body=None, resp=AsynchrTask(), name="delNic")
        return response   
    
    def modifyNic(self, nicUri, req=ModifyNicReq()):
        '''
        function:修改网卡属性
        '''
        response = client.send(method='PUT', url=nicUri, body=dict(req), resp=None, name="modifyNic")
        return response 
    
    def attachVol(self, vmUri, req=AttachVolReq()):
        '''
        function:挂载磁盘卷
        '''
        response = client.send(method='POST', url=vmUri + "/action/attachvol", body=dict(req), resp=AsynchrTask(), name="attachVol")
        return response     
    
    def detachVol(self, vmUri, req=DetachVolReq()):
        '''
        function:卸载磁盘卷
        '''
        response = client.send(method='POST', url=vmUri + "/action/detachvol", body=dict(req), resp=AsynchrTask(), name="detachVol")
        return response
    
    def attachTools(self, vmUri):
        '''
        function:挂载tools
        '''
        response = client.send(method='POST', url=vmUri + "/action/installtools", body=None, resp=AsynchrTask(), name="attachCdrom")
        return response
    
    def detachTools(self, vmUri):
        '''
        function:卸载tools
        '''
        response = client.send(method='POST', url=vmUri + "/action/uninstalltools", body=None, resp=AsynchrTask(), name="detachTools")
        return response
    
    def createVmSnapshot(self, vmUri, req=CreateVmSnapshotReq()):
        '''
        function:创建虚拟机快照
        '''
        response = client.send(method='POST', url=vmUri + "/snapshots", body=dict(req), resp=VmTaskResp(), name="createVmSnapshot")
        return response
    
    def listVmSnapshots(self, vmUri):
        '''
        function:查询指定虚拟机的快照列表
        '''
        response = client.send(method='GET', url=vmUri + "/snapshots", body=None, resp=ListVmSnapshotsResp(), name="listVmSnapshots")
        return response
    
    def queryVmSnapshot(self, snapshotUri, refreshflag=None):
        '''
        function:查询指定的虚拟机快照信息
        '''
        if refreshflag :
            snapshotUri += "?" + str(refreshflag)
        response = client.send(method='GET', url=snapshotUri, body=None, resp=QueryVmSnapshotResp(), name="queryVmSnapshot")
        return response
    
    def deleteVmSnapshot(self, snapshotUri):
        '''
        function:删除指定虚拟机快照
        '''
        response = client.send(method='DELETE', url=snapshotUri, body=None, resp=AsynchrTask(), name="deleteVmSnapshot")
        return response
    
    def cloneVm(self, vmUri, req=CloneVmReq()):
        '''
        function:虚拟机转化成模板
        '''
        response = client.send(method='POST', url=vmUri + "/action/clone", body=dict(req), resp=VmTaskResp(), name="cloneVm")
        return response   
    
    def importVm(self, siteUri, req=ImportVmTempReq()):
        '''
        function:导入模板
        '''
        response = client.send(method='POST', url=siteUri + "/vms/action/import", body=dict(req), resp=VmTaskResp(), name="importVm")
        return response
    
    def exportVm(self, vmUri, req=ExportVmTempReq()):
        '''
        function:导出模板
        '''
        response = client.send(method='POST', url=vmUri + "/action/export", body=dict(req), resp=VmTaskResp(), name="exportVm")
        return response
    
    def listOsInfos(self, siteUri):
        '''
        function:查询系统支持的虚拟机操作系统
        '''
        response = client.send(method='GET', url=siteUri + "/vms/osversions", body=None, resp=ListOsInfosResp(), name="listOsInfos")
        return response
