# modelo para pegar dados do zabbix 
    
# -*- coding: utf-8 -*- 
from zabbix_api import ZabbixAPI
from datetime import datetime
import time

zapi = ZabbixAPI("*********************************")
zapi.session.verify = False
zapi.timeout = 10.0
zapi.login("USER", "PASS")

# regra de conexao 
print("Connected to Zabbix API Version %s" % zapi.api_version())

# Vou utilizar neste caso somente itens pertinentes ao Azure AppInsight
item_id_0 = 2916801  # DEGUST Quantidade BOM financeiro_Degust_BOM
item_id_1 = 2916802  # DEGUST Quantidade BOM login_Degust_BOM
item_id_2 = 2916803  # DEGUST Quantidade BOM Update_Degust_BOM
item_id_3 = 2916804  # DEGUST Quantidade BOM venda_Degust_BOM
item_id_4 = 2916797  # DEGUST Quantidade Excelente financeiro_Degust_Excelente
item_id_5 = 2916798  # DEGUST Quantidade Excelente login_Degust_Excelente
item_id_6 = 2916799  # DEGUST Quantidade Excelente Update_Degust_Excelente
item_id_7 = 2916800  # DEGUST Quantidade Excelente venda_Degust_Excelente
item_id_8 = 2916805  # DEGUST Quantidade RUIM financeiro_Degust_RUIM
item_id_9 = 2916806  # DEGUST Quantidade RUIM login_Degust_RUIM
item_id_10 = 2916807  # DEGUST Quantidade RUIM Update_Degust_RUIM
item_id_11 = 2916808  # DEGUST Quantidade RUIM venda_Degust_RUIM
item_id_12 = 2916809  # DEGUST Quantidade TODAS financeiro_Degust_TODAS
item_id_13 = 2916810  # DEGUST Quantidade TODAS login_Degust_TODAS
item_id_14 = 2916811  # DEGUST Quantidade TODAS Update_Degust_TODAS
item_id_15 = 2916812  # DEGUST Quantidade TODAS venda_Degust_TODAS

item_id_16 = 2915776  # MVX Quantidade BOM ERP_Requests_com_sucesso_maior_2seg_menor_3seg_BOM
item_id_17 = 2915777  # MVX Quantidade BOM Requests_login_maior_2seg_menor_3seg_BOM
item_id_18 = 2915778  # MVX Quantidade BOM Requests_SincronizacaoPOS_entre_7seg_12seg_BOM
item_id_19 = 2915779  # MVX Quantidade Excelente ERP_Requests_com_sucesso_maior_3seg_Excelente
item_id_20 = 2915780  # MVX Quantidade Excelente Requests_login_maior_3seg_Excelente
item_id_21 = 2915781  # MVX Quantidade Excelente Requests_SincronizacaoPOS_12seg_Excelente
item_id_22 = 2915773  # MVX Quantidade RUIM ERP_Requests_com_sucesso_maior_3seg_RUIM
item_id_23 = 2915774  # MVX Quantidade RUIM Requests_login_maior_3seg_RUIM
item_id_24 = 2915775  # MVX Quantidade RUIM Requests_SincronizacaoPOS_12seg_RUIM
item_id_25 = 2915770  # MVX Quantidade TODOS ERP_Requests_com_sucesso_TODAS
item_id_26 = 2915771  # MVX Quantidade TODOS Requests_login_TODOS
item_id_27 = 2915772  # MVX Quantidade TODOS Requests_SincronizacaoPOS_TODOS

item_id_28 = 2918793 # OPUS Quantidade BOM agenda-OPUS_BOM
item_id_29 = 2918794 # OPUS Quantidade BOM bi-OPUS_BOM
item_id_30 = 2918795 # OPUS Quantidade BOM lancamentos-OPUS_BOM
item_id_31 = 2918796 # OPUS Quantidade BOM liquidacao-OPUS_BOM
item_id_32 = 2918797 # OPUS Quantidade BOM login-OPUS_BOM
item_id_33 = 2918798 # OPUS Quantidade BOM pessoa-OPUS_BOM
item_id_34 = 2918799 # OPUS Quantidade BOM titulos-OPUS_BOM
item_id_35 = 2918800 # OPUS Quantidade BOM vendas-OPUS_BOM
item_id_36 = 2918801 # OPUS Quantidade Excelente agenda-OPUS_Excelente
item_id_37 = 2918802 # OPUS Quantidade Excelente bi-OPUS_Excelente
item_id_38 = 2918803 # OPUS Quantidade Excelente lancamentos-OPUS_Excelente
item_id_39 = 2918804 # OPUS Quantidade Excelente liquidacao-OPUS_Excelente
item_id_40 = 2918805 # OPUS Quantidade Excelente login-OPUS_Excelente
item_id_41 = 2918806 # OPUS Quantidade Excelente pessoa-OPUS_Excelente
item_id_42 = 2918807 # OPUS Quantidade Excelente titulos-OPUS_Excelente
item_id_43 = 2918808 # OPUS Quantidade Excelente vendas-OPUS_Excelente
item_id_44 = 2918809 # OPUS Quantidade RUIM agenda-OPUS_RUIM
item_id_45 = 2918810 # OPUS Quantidade RUIM bi-OPUS_RUIM
item_id_46 = 2918811 # OPUS Quantidade RUIM lancamentos-OPUS_RUIM
item_id_47 = 2918812 # OPUS Quantidade RUIM liquidacao-OPUS_RUIM
item_id_48 = 2918813 # OPUS Quantidade RUIM login-OPUS_RUIM
item_id_49 = 2918814 # OPUS Quantidade RUIM pessoa-OPUS_RUIM
item_id_50 = 2918815 # OPUS Quantidade RUIM titulos-OPUS_RUIM
item_id_51 = 2918816 # OPUS Quantidade RUIM vendas-OPUS_RUIM
item_id_52 = 2918817 # OPUS Quantidade TODOS agenda-OPUS_TODOS
item_id_53 = 2918818 # OPUS Quantidade TODOS bi-OPUS_TODOS
item_id_54 = 2918819 # OPUS Quantidade TODOS lancamentos-OPUS_TODAS
item_id_55 = 2918820 # OPUS Quantidade TODOS liquidacao-OPUS_TODOS
item_id_56 = 2918821 # OPUS Quantidade TODOS login-OPUS_TODOS
item_id_57 = 2918822 # OPUS Quantidade TODOS pessoa-OPUS_TODOS
item_id_58 = 2918823 # OPUS Quantidade TODOS titulos-OPUS_TODOS
item_id_59 = 2918824 # OPUS Quantidade TODOS vendas-OPUS_TODOS

item_id_60 = 2915558 # Seller - Metricas - Quantidade Bom consulta_a_vendas_Comissao_quantidade_DIA_Bom
item_id_61 = 2915605 # Seller - Metricas - Quantidade Bom consulta_a_vendas_Diarias_quantidade_Bom
item_id_62 = 2915610 # Seller - Metricas - Quantidade Bom consulta_a_vendas_Realizada_quantidade_Bom
item_id_63 = 2915611 # Seller - Metricas - Quantidade Bom Livros_Fiscais_quantidade_DIA_Bom
item_id_64 = 2915612 # Seller - Metricas - Quantidade Bom login_quantidade_Bom
item_id_65 = 2915645 # Seller - Metricas - Quantidade Bom Manter_lancamentos_quantidade_Bom
item_id_66 = 2915646 # Seller - Metricas - Quantidade Bom Pesquisa_lancamentos_quantidade_DIA_Bom
item_id_67 = 2915647 # Seller - Metricas - Quantidade Excelente consulta_a_vendas_Comissao_quantidade_DIA_excelente
item_id_68 = 2915648 # Seller - Metricas - Quantidade Excelente consulta_a_vendas_Diarias_quantidade_excelente
item_id_69 = 2915649 # Seller - Metricas - Quantidade Excelente consulta_a_vendas_Realizada_quantidade_excelente
item_id_70 = 2915650 # Seller - Metricas - Quantidade Excelente Livros_Fiscais_quantidade_DIA_excelente
item_id_71 = 2915651 # Seller - Metricas - Quantidade Excelente login_quantidade_excelente
item_id_72 = 2915652 # Seller - Metricas - Quantidade Excelente Manter_lancamentos_quantidade_excelente
item_id_73 = 2915653 # Seller - Metricas - Quantidade Excelente Pesquisa_lancamentos_quantidade_DIA_excelente
item_id_74 = 2915654 # Seller - Metricas - Quantidade Ruim consulta_a_vendas_Comissao_quantidade_DIA_Ruim
item_id_75 = 2915655 # Seller - Metricas - Quantidade Ruim consulta_a_vendas_Diarias_quantidade_Ruim
item_id_76 = 2915656 # Seller - Metricas - Quantidade Ruim consulta_a_vendas_Realizada_quantidade_Ruim
item_id_77 = 2915657 # Seller - Metricas - Quantidade Ruim Livros_Fiscais_quantidade_DIA_Ruim
item_id_78 = 2915658 # Seller - Metricas - Quantidade Ruim login_quantidade_Ruim
item_id_79 = 2915659 # Seller - Metricas - Quantidade Ruim Manter_lancamentos_quantidade_Ruim
item_id_80 = 2915660 # Seller - Metricas - Quantidade Ruim Pesquisa_lancamentos_quantidade_DIA_Ruim
item_id_81 = 2914168 # Seller - Metricas - Quantidade TOTAL consulta_a_vendas_Comissao_quantidade_DIA
item_id_82 = 2914167 # Seller - Metricas - Quantidade TOTAL consulta_a_vendas_Diarias_quantidade
item_id_83 = 2914162 # Seller - Metricas - Quantidade TOTAL consulta_a_vendas_Realizada_quantidade
item_id_84 = 2914171 # Seller - Metricas - Quantidade TOTAL Livros_Fiscais_quantidade_DIA
item_id_85 = 2914164 # Seller - Metricas - Quantidade TOTAL login_quantidade
item_id_86 = 2914161 # Seller - Metricas - Quantidade TOTAL Manter_lancamentos_quantidade
item_id_87 = 2914175 # Seller - Metricas - Quantidade TOTAL Pesquisa_lancamentos_quantidade_DIA

item_id_88 = 2916581 # UX Quantidade BOM AuthenticateJson_BOM
item_id_89 = 2916582 # UX Quantidade BOM Estoque_BOM
item_id_90 = 2916583 # UX Quantidade BOM NotaFiscal_BOM
item_id_91 = 2916584 # UX Quantidade BOM OmniWebAPI_BOM
item_id_92 = 2916585 # UX Quantidade Excelente AuthenticateJson_Excelente
item_id_93 = 2916586 # UX Quantidade Excelente Estoque_Excelente
item_id_94 = 2916587 # UX Quantidade Excelente NotaFiscal_Excelente
item_id_95 = 2916588 # UX Quantidade Excelente OmniWebAPI_Excelente
item_id_96 = 2916592 # UX Quantidade RUIM AuthenticateJson_RUIM
item_id_97 = 2916591 # UX Quantidade RUIM Estoque_RUIM
item_id_98 = 2916590 # UX Quantidade RUIM NotaFiscal_RUIM
item_id_99 = 2916589 # UX Quantidade RUIM OmniWebAPI_RUIM
item_id_100 = 2916593 # UX Quantidade TOTAL AuthenticateJson_TODAS
item_id_101 = 2916594 # UX Quantidade TOTAL Estoque_TODAS
item_id_102 = 2916595 # UX Quantidade TOTAL NotaFiscal_TODAS
item_id_103 = 2916596 # UX Quantidade TOTAL OmniWebAPI_TODAS


# Inicio do processo para salvar os dados.

historico = zapi.history.get({ 'itemids': [ item_id_0 ], 
'history': 3, 
'output': 'extend',
'limit': 1
    })


for point in historico:       # Ver uma possibilidade logica de colocar um looping aqui pois alguns dados podem ter mais de uma amostra no mesmo periodo isso é um saco!!!!
    # tem que converter o dado da API para manter em variavel
    dtItem = ("{0}".format(datetime.fromtimestamp(int(point['clock'])).strftime("%x %X"), point['value']))
    valorItem = ('{1}'.format(datetime.fromtimestamp(int(point['value'])).strftime("%x %X"), point['value']))
    print (point)


