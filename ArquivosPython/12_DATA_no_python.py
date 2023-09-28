# %%

import datetime

# %%

# 01 - RECUPERANDO DATAS

data_com_hora = datetime.datetime.now()

print(data_com_hora)

data_sem_hora = datetime.date.today()

print(data_sem_hora)

# %%

# 02 - DIVIDINDO ESSA DATA RECUPERADA (ANO / MES / DIA)

ano = str(data_sem_hora.year)

mes = str(data_sem_hora.month)

dia = str(data_sem_hora.day)

print('ano: ' + ano )
print('mes: ' + mes )
print('dia: ' + dia )

# %%

# 03 - CONCATENANDO COLUNAS PARA FORMAR UMA DATA

ano = data_sem_hora.year
mes = data_sem_hora.month
dia = data_sem_hora.day

nova_data = datetime.datetime(ano, mes, dia)

print(nova_data)

nova_data_sem_hora = datetime.date(ano, mes, dia)

print(nova_data_sem_hora)

# %%

# 04 - EXTRAIR DE UMA DATA INFORMAÇÕES DE HORA / MINUTO / SEGUNDO

hora_completa = data_com_hora.time()

print(hora_completa)

hora = hora_completa.hour

minuto = hora_completa.minute

segundo = hora_completa.second

print('hora: ' + str(hora))
print('minuto: ' + str(minuto))
print('segundo: ' + str(segundo))


# %%

# 05 - IDENTIFICANDO QUAL O DIA DA SEMANA 

#strftime()

# DOMINGO À SÁBADO
dia_da_semana = data_com_hora.strftime('%A') 

print(dia_da_semana)

# 0 - Domingo / 6 - Sábado
dia_da_semana_numerico = data_com_hora.strftime('%w')

print(dia_da_semana_numerico)

# Mês por Extenso

mes_por_extenso = data_com_hora.strftime('%B')

print(mes_por_extenso)

# Qual (26/09/2023) o dia do ano que estamos?

dia_do_ano = data_com_hora.strftime('%j')

print(dia_do_ano)

# Qual (26/09/2023) a semana do ano que estamos?

semana_do_ano = data_com_hora.strftime('%U')

print(semana_do_ano)


# %%

# 06 - SUBTRAÇÃO E ADIÇÃO DE DDIAS EM UMA DATA

#fromordinal()

# ADICIONAR 10 DIAS NA NOSSA DATA - 26/09/2023 + 10 DIAS = 06/10/2023

v = 1

data_futura = datetime.date.fromordinal(data_sem_hora.toordinal()+v)

print(data_futura)

# REMOVER 10 DIAS NA NOSSA DATA - 26/09/2023 + 10 DIAS = 16/09/2023

data_passada = datetime.date.fromordinal(data_sem_hora.toordinal()-v)

print(data_passada)

# %%
