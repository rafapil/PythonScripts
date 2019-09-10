# -*- coding: utf-8 -*- 
from zabbix_api import ZabbixAPI
from datetime import datetime
import time
# bases salvando no banco essa porra 
import mysql.connector

from mysql.connector import errorcode 

# obtendo conection string 
config = {
    'host':'*****************',
    'user':'API',
    'password':'***********',
    'database':'***********'
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

zapi = ZabbixAPI("***************************")
# Disable SSL certificate verification
zapi.session.verify = False
# Specify a timeout (in seconds)
zapi.timeout = 10.1
# informacoes de acesso
zapi.login("USER", "PASS")
# mostra versao do zabbix
print("Connected to Zabbix API Version %s" % zapi.api_version())

# aqui tem que passar o ID do item (pensar pq são uma porrada de itens uma forma bonita é melhor que fazer um catado obvio)
# MIDe
item_id_0 = 2212476   # Tempo MID_central_5min
item_id_1 = 2212479   # Tempo MID6_central_5min
item_id_2 = 2212481   # Tempo MID4_central_5min
item_id_3 = 2212483   # Tempo MID5_central_5min
item_id_4 = 2198455   # Contingencia_MIDCentral_60min
item_id_5 = 2198498   # Contingencia_MID_mide6_60min
item_id_6 = 2199995   # Offline_MID_mide6
item_id_7 = 2198369   # Contingencia_MID_azure_mide4_60min
item_id_8 = 2198412   # Contingencia_MID_azure_mide5_60min
# DTEF
item_id_9 = 2003427   # Tempo Autorização (LINX + ADQ)
# Microvix
item_id_10 = 917847   # Tempo ERP Microvix
item_id_11 = 2156697  # Tempo POS Microvix
item_id_12 = 2184022  # Tempo Sincronização do PDV
item_id_13 = 878233   # Transacional MVX PROD1 
item_id_14 = 878234   # Transacional MVX PROD2 
item_id_15 = 878235   # Transacional MVX PROD3  
item_id_16 = 878236   # Transacional MVX PROD4  
item_id_17 = 878237   # Transacional MVX PROD5  
item_id_18 = 878238   # Transacional MVX PROD6  
item_id_19 = 878239   # Transacional MVX PROD7  
item_id_20 = 878240   # Transacional MVX PROD8  
item_id_21 = 878241   # Transacional MVX PROD9  
item_id_22 = 878242   # Transacional MVX PROD10  
item_id_23 = 878243   # Transacional MVX PROD11  
item_id_24 = 878244   # Transacional MVX PROD12  
item_id_25 = 878245   # Transacional MVX PROD13  
item_id_26 = 878246   # Transacional MVX PROD14  
# UX
item_id_27 = 2031527  # Tempo Aut UX - Autenticacao - Azure
item_id_28 = 2050988  # Tempo Aut UX - Atenticacao - AMC
item_id_29 = 2098521  # Tempo Aut UX - Atenticacao - DLG
item_id_30 = 2098515  # Tempo Aut UX - Atenticacao - LNX
item_id_31 = 2031579  # Tempo App UX - Application
item_id_32 = 2050982  # Tempo App UX - Application - Azure AMC
item_id_33 = 2098496  # Tempo App UX - Application - Azure - DLG
item_id_34 = 2098508  # Tempo App UX - Application - Azure - LNX
item_id_35 = 2031567  # Tempo PORTAL UX - PORTAL - Azure
item_id_36 = 2050975  # Tempo PORTAL UX - PORTAL - Azure AMC
item_id_37 = 2098563  # Tempo PORTAL UX - PORTAL - Azure - DLG
item_id_38 = 2098575  # Tempo PORTAL UX - PORTAL - Azure - LNX
# Analytics
item_id_39 = 1970492  # Tempo de Autenticação
item_id_40 = 1970501  # Tempo Desempenho View Gerente
item_id_41 = 1970495  # Tempo Desempenho View Executivo
# OPUS
item_id_42 = 1879138  # Tempo Linx Estetica Login
item_id_43 = 1879174  # Tempo Linx Estetica - Consulta Vendas
item_id_44 = 1879375  # Tempo Linx Estetica - Consulta Titulos
item_id_45 = 1879411  # Tempo Linx Estetica - Consulta Liquidacao
item_id_46 = 1956402  # Tempo Linx Estetica - Consulta Pessoa
item_id_47 = 1956426  # Tempo Linx Estetica - Consulta de Agendamentos
item_id_48 = 1956450  # Tempo Linx Estetica - Consulta de Lancamentos
item_id_49 = 1879144  # Tempo Linx Ensino Login
item_id_50 = 1879180  # Tempo Linx Ensino - Consulta Vendas
item_id_51 = 1879381  # Tempo Linx Ensino - Consulta Titulos
item_id_52 = 1879417  # Tempo Linx Ensino - Consulta Liquidacao
item_id_53 = 1956408  # Tempo Linx Ensino - Consulta Pessoa
item_id_54 = 1956456  # Tempo Linx Ensino - Consulta de lancamentos
item_id_55 = 1879150  # Tempo Linx Lavanderias Login
item_id_56 = 1879186  # Tempo Linx Lavanderias - Consulta Vendas
item_id_57 = 1879387  # Tempo Linx Lavanderias - Consulta Titulos
item_id_58 = 1879423  # Tempo Linx Lavanderias - Consulta Liquidacao
item_id_59 = 1956414  # Tempo Linx Lavanderias - Consulta Pessoa
item_id_60 = 1956462  # Tempo Linx Lavanderias - Consulta de Lancamentos
#Degust
item_id_61 = 2089008  # Tempo GERAL_carregarLojas
item_id_62 = 2089007  # Tempo GERAL_carregarPerfis
item_id_63 = 2089006  # Tempo GERAL_obterChaveAcesso
item_id_64 = 2089005  # Tempo GERAL_validarSenha
item_id_65 = 2089004  # Tempo GERAL_validarLogin
item_id_66 = 2089087  # Tempo VAREJO_carregarLojas
item_id_67 = 2089086  # Tempo VAREJO_carregarPerfis
item_id_68 = 2089085  # Tempo VAREJO_obterChaveAcesso
item_id_69 = 2089084  # Tempo VAREJO_validarSenha
item_id_70 = 2089083  # Tempo VAREJO_validarLogin
# Rezende
item_id_71 = 878353  # Tempo LM10-B1-EMSYS: Performance
item_id_72 = 878354  # Tempo LM10-B3-EMSYS: Performance
item_id_73 = 878356  # Tempo LM11-B3-EMSYS: Performance
item_id_74 = 878358  # Tempo LM12-B3-EMSYS: Performance
item_id_75 = 878360  # Tempo LM13-B3-EMSYS: Performance
item_id_76 = 878366  # Tempo LM9-B3-EMSYS: Performance
item_id_77 = 1213617  # Tempo CTX-PG01-EMSYS: Performance
item_id_78 = 1213618  # Tempo LM14-B3-EMSYS: Performance
item_id_79 = 1213619  # Tempo LM15-B3-EMSYS: Performance
item_id_80 = 1213621  # Tempo XCH01-PG02-EMSYS: Performance
item_id_81 = 1213622  # Tempo XCH01-PG03-EMSYS: Performance
item_id_82 = 1213623  # Tempo XCH01-PG04-EMSYS: Performance
item_id_83 = 1213624  # Tempo XCH01-PG05-EMSYS: Performance
item_id_84 = 1213625  # Tempo XCH01-PG06-EMSYS: Performance
item_id_85 = 2182292  # Tempo emsysprd-vppg01-EMSYS: Performance
item_id_86 = 2182293  # Tempo emsysprd-vppg02-EMSYS: Performance
item_id_87 = 2182294  # Tempo emsysprd-vppg03-EMSYS: Performance
item_id_88 = 2182295  # Tempo emsysprd-vppg04-EMSYS: Performance
item_id_89 = 2182296  # Tempo emsysprd-vppg05-EMSYS: Performance
item_id_90 = 2182297  # Tempo emsysprd-vppg06-EMSYS: Performance
item_id_91 = 2182298  # Tempo emsysprd-vppg07-EMSYS: Performance
# BIG
item_id_92 = 1013762  # Tempo LNXBIGWEB08-BIGCONECTA
item_id_93 = 1013763  # Tempo LNXBIGWEB09-BIGCONECTA
item_id_94 = 1013764  # Tempo LNXBIGWEB07-BIGCONECTA
item_id_95 = 1013765  # Tempo LNXBIGWEB10-BIGCONECTA
item_id_96 = 1013766  # Tempo LNXBIGWEB11-BIGCONECTA
item_id_97 = 1013767  # Tempo LNXBIGDB07-BIGCONECTA
item_id_98 = 1013768  # Tempo LNXBIGDB08-BIGCONECTA
item_id_99 = 1013769  # Tempo LNXBIGDB09-BIGCONECTA
item_id_100 = 1013770  # Tempo LNXBIGDB10-BIGCONECTA
item_id_101 = 1013771  # Tempo LNXBIGDB11-BIGCONECTA
item_id_102 = 1933985  # Tempo LNXBIGDB16-BIGCONECTA
item_id_103 = 2183984  # Tempo LNXBIGDB18-BIGCONECTA
# Seller
item_id_104 = 2211250  # Tempo Seller_Tempo_Fun_0_Todos
item_id_105 = 2211251  # Tempo Seller_Tempo_Fun_16105_todos
item_id_106 = 2211262  # Tempo Seller_Tempo_Fun_16810_todos
item_id_107 = 2211260  # Tempo Seller_Tempo_Fun_17110_todos


# Criar o intervalo de coleta 
time_from = time.mktime(datetime.now().timetuple()) - 60 * 60 * 24  # 1 dia (inteiro)

#######################################################
# Aqui vai entrar a troca de sensores
#######################################################

#######################################################
# Produto MID 
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
# Produto Microvix
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
# Produto UX
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
# OPUS
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
# Degust
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
# Rezende
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
# BIG
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
# SELLER
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



