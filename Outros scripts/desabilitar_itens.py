# -*- coding: utf-8 -*- 
from zabbix_api import ZabbixAPI
from datetime import datetime
import urllib.request as urllib2
import time


zapi = ZabbixAPI("https://sm-fe01.webmonitor.global")
# Disable SSL certificate verification
#zapi.session.verify = False
# Specify a timeout (in seconds)
zapi.timeout = 30.1
# informacoes de acesso
# informacoes de acesso
zapi.login("linx.rafael", "stk456rfs")
# mostra versao do zabbix
print("Connected to Zabbix API Version %s" % zapi.api_version())

resultado = zapi.item.get({
    "groupids":"150", # O grupo deve ser informado nesta parte do código. 
    "filter":{
        "state":1
    },
    "output":[
        "hostid",
        "name",
        "itemid"
    ],
    "monitored": True  
})
#print('Quantidade de itens nao suportado, somente hosts ativos: ', resultado)
for x in resultado:
    zapi.item.update({'itemid': x ['itemid'],'status':1})




