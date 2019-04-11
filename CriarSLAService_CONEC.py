# outra vez hehe
#!/usr/bin/env python # -*- coding: utf-8 -*- 

import urllib.request as urllib2
from zabbix_api import ZabbixAPI 
zapi = ZabbixAPI(server="http://192.168.120.193/zabbix") 
zapi.login("Admin", "stk456rfs") 

def obterGrupos(): 
    listaGrupos = ['Templates/Server hardware', 'Virtual machines']
    return listaGrupos 
         
def obterGrupoId(nomeGrupo):
     groupId = zapi.hostgroup.get({ "output": "extend", "filter": { "name": nomeGrupo } })[0]['groupid']
     return groupId 
     
def obterHosts(nomeGrupo): 
    hosts_grupo = zapi.host.get({ "groupids": obterGrupoId(nomeGrupo), "output": [ "host" ] }) 
    listaHosts = [] 
    for x in hosts_grupo: listaHosts += [x['host']] 
    return listaHosts 
    
def obterHostId(nomeHost): 
    hostId = zapi.host.get({ "output": "hostid", "filter": { "host": nomeHost } })[0]['hostid']
    return hostId

def obterTriggersHosts(nomeHost): 
    triggers = zapi.trigger.get({ "hostids": obterHostId(nomeHost), "expandDescription": "true", "expandComment": "true", "expandExpression": "true" }) 
    for x in triggers: print (x['description']) 
        
def obterItens(nomeHost): 
    itens = zapi.item.get({ "hostids": obterHostId(nomeHost), "with_triggers": True, "selectTriggers": "extend" }) 
    listaItens = [] 
    for x in itens: listaItens += [x['name']] 
    return listaItens 
    
def obterItemTriggerId(nomeHost,nomeItem): 
    triggerId = zapi.item.get({ "output": "triggers","hostids": obterHostId(nomeHost), "with_triggers": True, "selectTriggers": "triggerid", "filter": { "name": nomeItem } })[0]['triggers'][0]['triggerid'] 
    return triggerId 
    
def criarServicosPai(nomeGrupo): 
    zapi.service.create({ "name": nomeGrupo, "algorithm": "1","showsla": "1", "goodsla": "99.99", "sortorder": "1" }) 
    
def obterServicosPai(nomeGrupo): 
    parentId = zapi.service.get({ "selectParent": "extend", "selectTrigger": "extend", "expandExpression": "true", "filter": { "name": nomeGrupo }})[0]['serviceid'] 
    return parentId 
    
def criarServicosFilho(nomeHost,nomeGrupo): 
    zapi.service.create({ "name": nomeHost, "algorithm": "1", "showsla": "1", "goodsla": "99.99", "sortorder": "1", "parentid": obterServicosPai(nomeGrupo)})

def obterServicosFilho(nomeHost): 
    parentIdChild = zapi.service.get({ "selectParent": "extend", "selectTrigger": "extend", "expandExpression": "true", "filter": { "name": nomeHost } })[0]['serviceid'] 
    return parentIdChild 
    
def criarItensServicos(nomeHost,nomeItem):
    zapi.service.create({ "name": nomeItem, "algorithm": "1", "showsla": "1", "goodsla": "99.99", "sortorder": "1", "parentid": obterServicosFilho(nomeHost), "triggerid": obterItemTriggerId(nomeHost,nomeItem)}) 
    
def obterServicos(): 
    itServices = zapi.service.get({ "selectParent": "extend", "selectTrigger": "extend" }) 
    listaServicos = [] 
    for x in itServices: listaServicos += [x['serviceid']] 
    return listaServicos 
    
def removerArvoreServicos(): 
    for x in obterServicos(): 
        zapi.service.deletedependencies([x]) 
        zapi.service.delete([x])

def criarArvoreServicos(): 
    removerArvoreServicos() 
    for nomeGrupo in obterGrupos(): 
        criarServicosPai(nomeGrupo) 
        for nomeHost in obterHosts(nomeGrupo): 
            criarServicosFilho(nomeHost, nomeGrupo) 
            for nomeItem in obterItens(nomeHost): 
                criarItensServicos(nomeHost, nomeItem)
criarArvoreServicos()

