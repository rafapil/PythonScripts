# -*- coding: utf-8 -*- 
from zabbix_api import ZabbixAPI
from datetime import datetime
import time
import urllib2


zapi = ZabbixAPI("https://sm-fe01.webmonitor.global")
# Disable SSL certificate verification
#zapi.session.verify = False
# Specify a timeout (in seconds)
zapi.timeout = 30.1
# informacoes de acesso
zapi.login("linx.rafael", "stk456rfs")
# mostra versao do zabbix
print("Connected to Zabbix API Version %s" % zapi.api_version())

resultado = zapi.item.get({'output': 'extend', 
    'filter': {
        'state': 1}, 'monitored': False})
print('Quantidade de itens nao suportado, somente hosts ativos: ', resultado)

itens = zapi.item.get({
    "groupids":"1115",
    "filter":{
        "state":1
    },
    "output":[
        "hostid",
        "name",
        "itemid"
    ]
    
})


#print "ID host - ID Item - Nome - Erro"

for x in itens:
    host = zapi.host.get({"hostids":x['hostid'],"output":["name"]})
    print x["hostid"], "|", host[0]["name"], "|", x["itemid"], "|", x["name"]

# print "Total de itens verificados com falha: ",len(itens)