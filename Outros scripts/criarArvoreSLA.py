# Criando arvore de SLA com todos os serviços de tudo que tem no zabbix 
#################################################

# -*- coding: utf-8 -*- 
from zabbix_api import ZabbixAPI
from datetime import datetime
import time
import urllib2


zapi = ZabbixAPI("http://192.168.120.193")
# Disable SSL certificate verification
#zapi.session.verify = False
# Specify a timeout (in seconds)
zapi.timeout = 30.1
# informacoes de acesso
zapi.login("Admin", "stk456rfs")
# mostra versao do zabbix
print("Connected to Zabbix API Version %s" % zapi.api_version())

def obterGrupos():
    hostgroups = zapi.hostgroup.get({
        'output':'extend',
        'real_hosts': True
    })

listaGrupos = []
for x in hostgroups:
    print x['name']
    listaGrupos += [x['name']]
return listaGrupos

def obterGruposId(nomeGrupo):
    groupId = zapi.hostgroup.get({
        'output':'extend',
        'filter':{
            'name': nomeGrupo
        }
    })[0]['groupid']
    return groupId

def obterHosts(nomeGrupo):
    hosts_grupo = zapi.host.get({
        'groupids': obterGruposId(nomeGrupo),
        'output': [
            'host'
        ]
    })

listaHosts = []
for x in hosts_grupo:
    print x['host']
    listaHosts += [x['host']]
return listaHosts

def obterHostId(nomeHost):
    hostId = zapi.host.get({
        'output': 'hostid',
        'filter';{
            'host':nomeHost
        }
    })[0]['hostid']
    return hostId 

def obterTriggersHosts(nomeHost): 
    triggers = zapi.trigger.get({
        'hostids': obterHostId(nomeHost),
        'expandDescription': 'true',
        'expandComment': 'true',
        'expandExpression': 'true'
    })
    for x in trigger:
        print x['description']

def obterItens(nomeHost):
    itens = zapi.Item.get({
        'hostids': obterHostId(nomeHost),
        'with_triggers': True,
        'selectTriggers': 'extend'
    })

    listaItens = []
    for x in itens:
        print x['name']
        listaItens += [x['name']]
    return listaItens

def obterItemTriggerId(nomeHost,nomeItem):
    triggerId = zapi.item.get({
        'output': 'triggers',
        'hostids': obterHostId(nomeHost),
        'with_triggers': True,
        'selectTriggers': 'triggerid',
        'filter':{
            'name': nomeItem
        }
    })[0]['triggers'][0][triggerId]
    return triggerId

def criarServicosPai(nomeGrupo):
    zapi.service.create({
        'name': nomeGrupo,
        'algorithm': '1',
        'showsla': '1',
        'goodsla': '99.99',
        'sortorder': '1'
    })

def obterServicosPai(nomeGrupo):
    parentId = zapi.service.get({
        'selectParent': 'extend',
        'selectTrigger': 'extend', 
        'expandExpression': 'true',
        'filter'{
            'name': nomeGrupo
        }
    })[0]['serviceid']
    return parentId

def criarServicosFilho(nomeHost,nomeGrupo):
    zapi.service.create({
        'name': nomeHost,
        'algorithm': '1',
        'showsla': '1',
        'goodsla': '99.99',
        'sortorder': '1',
        'parentid': obterServicosPai(nomeGrupo)
    })

def obterServicosFilho(nomeHost):
    parentIdChild = zapi.service.get({
        'selectParent': 'extend',
        'selectTrigger': 'extend',
        'expandExpression': 'true',
        'filter': {
            'name': nomeHost
        }
    })[0]['serviceid']
    return parentIdChild

def criarItensServicos(nomeHost,nomeItem): 
    zapi.service.create({ 
        'name': nomeItem, 
        'algorithm': '1', 
        'showsla': '1', 
        'goodsla': '99.99', 
        'sortorder': '1', 
        'parentid': obterServicosFilho(nomeHost),
        'triggerid': obterItemTriggerId(nomeHost,nomeItem)
    })

def obterServicos(): 
    itServices = zapi.service.get({ 
        'selectParent': 'extend', 
        'selectTrigger': 'extend' 
        }) 

        listaServicos = [] 
        for x in itServices: listaServicos += [x[‘serviceid’]] 
        return listaServicos 
        
    def removerArvoreServicos():
        for x in obterServicos(): 
            zapi.service.deletedependencies([x]) 
            zapi.service.delete([x])

    def criarArvoreServicos(): 
        removerArvoreServicos() 
        for nomeGrupo in obterGrupos(): criarServicosPai(nomeGrupo) 
            for nomeHost in obterHosts(nomeGrupo): 
                criarServicosFilho(nomeHost, nomeGrupo)

            for nomeItem in obterItens(nomeHost):
                criarItensServicos(nomeHost,nomeItem)
        criarArvoreServicos()


