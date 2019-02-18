# itens não suportado por grupo 
# -*- coding: utf-8 -*- 
from zabbix_api import ZabbixAPI
from datetime import datetime
import urllib.request
from urllib.request import urlopen
import time


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
    "groupids":"162",  # aqui deve ser alterado o ID do grupo que se deseja obter o valor. 
    "filter":{
        "state":0   # se for 0 significa itens ativos se for 1 significa itens inativos não suportados
    },
    #'monitored': True,
    "output":[
        "hostid",
        "name",
        "itemid"
    ]   
})

# print('Quantidade de itens nao suportado, somente hosts ativos: ', itens) # caso deseje ver os itens desmarque, pode causar bloq da ferramenta!!!
print('Quantidade de itens ativos: ',len(itens))
