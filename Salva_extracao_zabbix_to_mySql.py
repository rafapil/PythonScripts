# -*- coding: utf-8 -*- 
from zabbix_api import ZabbixAPI
from datetime import datetime
import time
# bases salvando no banco essa porra 
import mysql.connector

from mysql.connector import errorcode 

# obtendo conection string 
config = {
    'host':'endereco do host',
    'user':'usuario',
    'password':'senha',
    'database':'nome da base'
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

# A partir desse ponto vou iniciar a chamada para o zabbix (provavelmente vou usar um user generico da na mesma)

zapi = ZabbixAPI("URL do SERVIDOR ZABBIX")
# Disable SSL certificate verification
zapi.session.verify = False
# Specify a timeout (in seconds)
zapi.timeout = 10.1
# informacoes de acesso
zapi.login("usuario_zabbix_com_acesso_api", "usuario_zabbix")
# mostra versao do zabbix
print("Connected to Zabbix API Version %s" % zapi.api_version())

# aqui tem que passar o ID do item (pensar pq são varios itens uma forma bonita é melhor que fazer esse modelo)

item_id_0 = 2212476   # 
item_id_1 = 2212479   # 
item_id_2 = 2212481   # 
item_id_3 = 2212483   # 
item_id_4 = 2198455   # 
item_id_5 = 2198498   # 
item_id_6 = 2199995   # 
item_id_7 = 2198369   # 
item_id_8 = 2198412   # 

item_id_9 = 2003427   # 

item_id_10 = 917847   # 
item_id_11 = 2156697  # 
item_id_12 = 2184022  # 
item_id_13 = 878233   # 
item_id_14 = 878234   # 
item_id_15 = 878235   # 
item_id_16 = 878236   # 
item_id_17 = 878237   # 
item_id_18 = 878238   # 
item_id_19 = 878239   # 
item_id_20 = 878240   # 
item_id_21 = 878241   # 
item_id_22 = 878242   # 
item_id_23 = 878243   # 
item_id_24 = 878244   # 
item_id_25 = 878245   # 
item_id_26 = 878246   # 

item_id_27 = 2031527  # 
item_id_28 = 2050988  # 
item_id_29 = 2098521  # 
item_id_30 = 2098515  # 
item_id_31 = 2031579  # 
item_id_32 = 2050982  # 
item_id_33 = 2098496  # 
item_id_34 = 2098508  # 
item_id_35 = 2031567  # 
item_id_36 = 2050975  # 
item_id_37 = 2098563  # 
item_id_38 = 2098575  # 

item_id_39 = 1970492  # 
item_id_40 = 1970501  # 
item_id_41 = 1970495  # 

item_id_42 = 1879138  # 
item_id_43 = 1879174  # 
item_id_44 = 1879375  # 
item_id_45 = 1879411  # 
item_id_46 = 1956402  # 
item_id_47 = 1956426  # 
item_id_48 = 1956450  # 
item_id_49 = 1879144  # 
item_id_50 = 1879180  # 
item_id_51 = 1879381  # 
item_id_52 = 1879417  # 
item_id_53 = 1956408  # 
item_id_54 = 1956456  # 
item_id_55 = 1879150  # 
item_id_56 = 1879186  # 
item_id_57 = 1879387  # 
item_id_58 = 1879423  # 
item_id_59 = 1956414  # 
item_id_60 = 1956462  # 

item_id_61 = 2089008  # 
item_id_62 = 2089007  # 
item_id_63 = 2089006  # 
item_id_64 = 2089005  # 
item_id_65 = 2089004  # 
item_id_66 = 2089087  # 
item_id_67 = 2089086  # 
item_id_68 = 2089085  # 
item_id_69 = 2089084  # 
item_id_70 = 2089083  # 

item_id_71 = 878353   # 
item_id_72 = 878354   # 
item_id_73 = 878356   # 
item_id_74 = 878358   # 
item_id_75 = 878360   # 
item_id_76 = 878366   # 
item_id_77 = 1213617  # 
item_id_78 = 1213618  # 
item_id_79 = 1213619  # 
item_id_80 = 1213621  # 
item_id_81 = 1213622  # 
item_id_82 = 1213623  # 
item_id_83 = 1213624  # 
item_id_84 = 1213625  # 
item_id_85 = 2182292  # 
item_id_86 = 2182293  # 
item_id_87 = 2182294  # 
item_id_88 = 2182295  # 
item_id_89 = 2182296  # 
item_id_90 = 2182297  # 
item_id_91 = 2182298  # 

item_id_92 = 1013762  # 
item_id_93 = 1013763  # 
item_id_94 = 1013764  # 
item_id_95 = 1013765  # 
item_id_96 = 1013766  # 
item_id_97 = 1013767  # 
item_id_98 = 1013768  # 
item_id_99 = 1013769  # 
item_id_100 = 1013770  # 
item_id_101 = 1013771  # 
item_id_102 = 1933985  # 
item_id_103 = 2183984  # 

item_id_104 = 2211250  # 
item_id_105 = 2211251  # 
item_id_106 = 2211262  # 
item_id_107 = 2211260  # 


# Criar o intervalo de coleta 
time_from = time.mktime(datetime.now().timetuple()) - 60 * 5  # 5 min

#######################################################
# Aqui vai entrar a troca de sensores
#######################################################

#######################################################
# Produto 
#######################################################
historico = zapi.history.get({ 'itemids': [ item_id_0 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ('{1}'.format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 0, 1, 1, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

######################################################

historico = zapi.history.get({ 'itemids': [ item_id_1 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ('{1}'.format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 1, 1, 1, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

##############################################

historico = zapi.history.get({ 'itemids': [ item_id_2 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ('{1}'.format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 2, 1, 1, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#############################################

historico = zapi.history.get({ 'itemids': [ item_id_3 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ('{1}'.format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 3, 1, 1, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_4 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 4, 1, 1, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_5 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 5, 1, 1, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_6 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 6, 1, 1, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#########################################################

historico = zapi.history.get({ 'itemids': [ item_id_7 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 7, 1, 1, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

##########################################################

historico = zapi.history.get({ 'itemids': [ item_id_8 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 8, 1, 1, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")
    
#######################################################
# Produto Meios de Pagamento
#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_9 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 9, 2, 2, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################
# Produto 
#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_10 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 10, 3, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

########################################################

historico = zapi.history.get({ 'itemids': [ item_id_11 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 11, 3, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

########################################################

historico = zapi.history.get({ 'itemids': [ item_id_12 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 12, 3, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

########################################################

historico = zapi.history.get({ 'itemids': [ item_id_13 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 13, 3, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

########################################################

historico = zapi.history.get({ 'itemids': [ item_id_14 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 14, 3, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

########################################################

historico = zapi.history.get({ 'itemids': [ item_id_15 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 15, 3, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

########################################################

historico = zapi.history.get({ 'itemids': [ item_id_16 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 16, 3, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

########################################################

historico = zapi.history.get({ 'itemids': [ item_id_17 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 17, 3, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

########################################################

historico = zapi.history.get({ 'itemids': [ item_id_18 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 18, 3, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

########################################################

historico = zapi.history.get({ 'itemids': [ item_id_19 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 19, 3, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

########################################################

historico = zapi.history.get({ 'itemids': [ item_id_20 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 20, 3, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

########################################################

historico = zapi.history.get({ 'itemids': [ item_id_21 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 21, 3, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

########################################################

historico = zapi.history.get({ 'itemids': [ item_id_22 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 22, 3, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

########################################################

historico = zapi.history.get({ 'itemids': [ item_id_23 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 23, 3, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

########################################################

historico = zapi.history.get({ 'itemids': [ item_id_24 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 24, 3, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

########################################################

historico = zapi.history.get({ 'itemids': [ item_id_25 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 25, 3, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

########################################################

historico = zapi.history.get({ 'itemids': [ item_id_26 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 26, 3, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################
# Produto 
#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_27 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 27, 4, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_28 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 28, 4, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_29 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 29, 4, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_30 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 30, 4, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_31 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 31, 4, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_32 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 32, 4, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_33 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 33, 4, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_34 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 34, 4, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_35 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 35, 4, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_36 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 36, 4, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_37 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 37, 4, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_38 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 38, 4, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

#######################################################
# Analytics
#######################################################

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_39 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 39, 5, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_40 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 40, 5, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_41 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 41, 5, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

#######################################################
# Produto
#######################################################

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_42 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 42, 6, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_43 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 43, 6, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_44 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 44, 6, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_45 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 45, 6, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_46 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 46, 6, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_47 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 47, 6, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_48 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 48, 6, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_49 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 49, 6, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_50 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 50, 6, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_51 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 51, 6, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_52 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 52, 6, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_53 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 53, 6, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_54 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 54, 6, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_55 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 55, 6, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_56 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 56, 6, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_57 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 57, 6, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_58 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 58, 6, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_59 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 59, 6, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_60 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 60, 6, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

#######################################################
# Produto
#######################################################

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_61 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 61, 7, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_62 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 62, 7, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_63 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 63, 7, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_64 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 64, 7, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_65 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 65, 7, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_66 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 66, 7, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################
historico = zapi.history.get({ 'itemids': [ item_id_67 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 67, 7, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_68 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 68, 7, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_69 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 69, 7, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_70 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 70, 7, 3, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

#######################################################
# Produto
#######################################################

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_71 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 71, 8, 4, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_72 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 72, 8, 4, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_73 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 73, 8, 4, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_74 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 74, 8, 4, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_75 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 75, 8, 4, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_76 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 76, 8, 4, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_77 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 77, 8, 4, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_78 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 78, 8, 4, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_79 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 79, 8, 4, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_80 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 80, 8, 4, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_81 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 81, 8, 4, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_82 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 82, 8, 4, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_83 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 83, 8, 4, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_84 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 84, 8, 4, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_85 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 85, 8, 4, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_86 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 86, 8, 4, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_87 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 87, 8, 4, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_88 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 88, 8, 4, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_89 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 89, 8, 4, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_90 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 90, 8, 4, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_91 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 91, 8, 4, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

#######################################################
# Produto
#######################################################

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_92 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 92, 9, 5, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_93 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 93, 9, 5, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_94 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 94, 9, 5, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_95 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 95, 9, 5, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_96 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 96, 9, 5, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_97 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 97, 9, 5, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_98 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 98, 9, 5, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_100 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 100, 9, 5, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_101 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 101, 9, 5, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_102 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 102, 9, 5, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_103 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 103, 9, 5, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

#######################################################
# Produto
#######################################################

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_104 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 104, 10, 4, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_105 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 105, 10, 4, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_106 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 106, 10, 4, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

#######################################################

historico = zapi.history.get({ 'itemids': [ item_id_107 ], 
'history': 0, 
'output': 'extend', 
'time_from': time_from, 
    }) 

for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ("{1}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))

    # Inserir os dados na tabela (preferivel já ter mapeada)
    cursor.execute("INSERT INTO kpi (kpi_dttime, kpi_itemID, kpi_itemProduto, kpi_itemVertical, kpi_itemValor) VALUES (%s, %s, %s, %s, %s);", (dtItem, 107, 10, 4, valorItem))
    print("Inserted",cursor.rowcount,"row(s) of data.")

# Cleanup
conn.commit()
cursor.close()
conn.close()
print("Done.")



