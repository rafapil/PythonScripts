# -*- coding: utf-8 -*- 
from zabbix_api import ZabbixAPI
from datetime import datetime
import time
# bases salvando no banco essa porra 
import mysql.connector

from mysql.connector import errorcode 

# obtendo conection string 
config = {
    'host':'*************',
    'user':'API',
    'password':'********',
    'database':'*********'
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

#Zabbix conf
zapi = ZabbixAPI("***************************************")

zapi.session.verify = True

zapi.timeout = 10.1

zapi.login("USER", "PASS")

print("Connected to Zabbix API Version %s" % zapi.api_version())

# Itens 
item_id_0 = 2051339     # 878236    original  2051345
item_id_1 = 2051378   
item_id_2 = 2051384   
item_id_3 = 2051345   



# Criar o intervalo de coleta 
time_from = time.mktime(datetime.now().timetuple()) - 60 * 60 * 24 # 1 dia (inteiro)

#######################################################
# Aqui vai entrar a troca de sensores
#######################################################

#######################################################
# Sensores
#######################################################
historico = zapi.history.get({ 'itemids': [ item_id_0 ], 
'output': 'extend', 
'time_from': time_from
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['value'])).strftime("%x %X"), point['value']))
    # valorItem = ('{1}'.format(datetime.fromtimestamp(int(point['value'])).strftime("%x %X"), point['value']))
    # print (point)
    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO relatorio (rel_dttime, rel_itemvalor) VALUES (%s, %s);", (dtItem, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

##############################################

historico = zapi.history.get({ 'itemids': [ item_id_1 ], 
'output': 'extend', 
'time_from': time_from
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['value'])).strftime("%x %X"), point['value']))
    # valorItem = ('{1}'.format(datetime.fromtimestamp(int(point['value'])).strftime("%x %X"), point['value']))
    # print (point)
    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO relatorio (rel_dttime, rel_itemvalor) VALUES (%s, %s);", (dtItem, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

##############################################

historico = zapi.history.get({ 'itemids': [ item_id_2 ], 
'output': 'extend', 
'time_from': time_from
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['value'])).strftime("%x %X"), point['value']))
    # valorItem = ('{1}'.format(datetime.fromtimestamp(int(point['value'])).strftime("%x %X"), point['value']))
    # print (point)
    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO relatorio (rel_dttime, rel_itemvalor) VALUES (%s, %s);", (dtItem, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

##############################################

historico = zapi.history.get({ 'itemids': [ item_id_3 ], 
'output': 'extend', 
'time_from': time_from
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['value'])).strftime("%x %X"), point['value']))
    # valorItem = ('{1}'.format(datetime.fromtimestamp(int(point['value'])).strftime("%x %X"), point['value']))
    # print (point)
    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO relatorio (rel_dttime, rel_itemvalor) VALUES (%s, %s);", (dtItem, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

##############################################

# Cleanup
conn.commit()
cursor.close()
conn.close()
print("Done.")
