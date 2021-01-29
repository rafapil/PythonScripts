# itens não suportado salvando no mysql para consulta posteriormente. 

# -*- coding: utf-8 -*- 
from zabbix_api import ZabbixAPI
from datetime import datetime
import urllib.request as urllib2
import time
import mysql.connector
from mysql.connector import errorcode 

# conection string 
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'pass',
    'database':'relatorio'
}

# Construct connection string
try:
    conn = mysql.connector.connect(**config)
    print("Connection established")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor = conn.cursor()

zapi = ZabbixAPI("Zabbix-url")
# Disable SSL certificate verification
#zapi.session.verify = False
# Specify a timeout (in seconds)
zapi.timeout = 100.10
# informacoes de acesso
zapi.login("apizabbix", "apizabbix")
# mostra versao do zabbix
print("Connected to Zabbix API Version %s" % zapi.api_version())

resultado = zapi.item.get({'output': 'extend', 
    'filter': {
        'state': 1}, 'monitored': False})
print('Quantidade de itens nao suportado, somente hosts ativos: ', resultado)

itens = zapi.item.get({
    # "groupids":"1115", # O grupo deve ser informado nesta parte do código. 
    "filter":{
        "state":1
    },
    "output":[
        "hostid",
        "name",
        "itemid"
    ]
    
})

for x in itens:
    host = zapi.host.get({"hostids":x['hostid'],"output":["name"]})
    cursor.execute("INSERT INTO relatorio.naosuportado (hostid_nsz, host_nsz, itemid_nsz, itemname_nsz) VALUES (%s, %s, %s, %s);", (x["hostid"], host[0]["name"], x["itemid"], x["name"]))
    print("Inserido",cursor.rowcount,"row(s)")

# Cleanup
conn.commit()
cursor.close()
conn.close()
print("Done.")