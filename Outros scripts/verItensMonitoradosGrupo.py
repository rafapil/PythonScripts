# itens não suportado por grupo 

# -*- coding: utf-8 -*- 
import urllib.request as urllib2
from zabbix_api import ZabbixAPI 

zapi = ZabbixAPI("https://sm-fe01.webmonitor.global")
# Disable SSL certificate verification
#zapi.session.verify = False
# Specify a timeout (in seconds)
zapi.timeout = 30.1
# informacoes de acesso
zapi.login("linx.rafael", "stk456rfs")
# mostra versao do zabbix
print("Connected to Zabbix API Version %s" % zapi.api_version())

itens = zapi.item.get({ 
    "output": "extend", 
    "filter": {
        "state": 1 }
         })


print('Quantidade de itens nao suportado, somente hosts ativos: ',len(itens))