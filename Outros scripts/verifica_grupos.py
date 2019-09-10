# outra vez hehe
#!/usr/bin/env python # -*- coding: utf-8 -*- 

import urllib.request as urllib2
from zabbix_api import ZabbixAPI 
zapi = ZabbixAPI(server="*****************************") 
zapi.login("USER", "PASS") 

print("Connected to Zabbix API Version %s" % zapi.api_version())

def obterGrupos(): 
    hostgroups = zapi.hostgroup.get({ "output": "extend", "real_hosts": True })
    listaGrupos = [] 
    for x in hostgroups: listaGrupos += [x['name']]
    # listaGrupos = ['Virtual machines']
    return listaGrupos 
         
def obterGrupoId(nomeGrupo):
     groupId = zapi.hostgroup.get({ "output": "extend", "filter": { "name": nomeGrupo } })[0]['groupid']
     return groupId 
     
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
    # removerArvoreServicos() 
    for nomeGrupo in obterGrupos(): 
        print(nomeGrupo)
    #    for igGrupo in obterGrupoId(nomeGrupo):
    #        print (igGrupo)
        #for nomeHost in obterHosts(nomeGrupo): 
            #criarServicosFilho(nomeHost, nomeGrupo) 
            #for nomeItem in obterItens(nomeHost): 
                #criarItensServicos(nomeHost, nomeItem)
criarArvoreServicos()