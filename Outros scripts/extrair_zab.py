# -*- coding: utf-8 -*- 
from zabbix_api import ZabbixAPI
from datetime import datetime
import time


zapi = ZabbixAPI("https://endereco.com.br/zabbix")
# Disable SSL certificate verification
zapi.session.verify = False
# Specify a timeout (in seconds)
zapi.timeout = 10.1
# informacoes de acesso
zapi.login("usuario.zabbix", "senhaUsuario")
# mostra versao do zabbix
print("Connected to Zabbix API Version %s" % zapi.api_version())

for hosts in zapi.host.get({'output': ['host','interface']}):
    print(hosts)

#item_id = 1879051

# Create a time range
#time_till = time.mktime(datetime.now().timetuple())
#time_from = time_till - 60 * 60 * 4  # 4 hours

#time_from = time.mktime(datetime.now().timetuple()) - 60 * 5  # 5 min


#historico = zapi.history.get({ 'itemids': [ item_id ], 
#'history': 0, 
#'output': 'extend', 
#'time_from': time_from, 
#'time_till': “1439250959” 
#    }) 

# Print out each datapoint
#for point in historico:
#    print("{0}: {1}".format(datetime.fromtimestamp(int(point['clock']))
#                            .strftime("%x %X"), point['value']))

# 0 pertence a data 
# 1 pertence a valor 


