# %%

# Etapa 01 - Instalação das Bibliotecas 

## yahoo-finance (yfinance)

#!pip install yfinance

## pandas-datareader (pandas_datareader)

#!pip install pandas_datareader

# %% 

################################################################################################

# Etapa 02 - Importação de Bibliotecas

import pandas as pd
import pandas_datareader.data as web
import yfinance as yf
yf.pdr_override()
from datetime import datetime

# %%

################################################################################################

# Etapa 03 - Definição de Variáveis

nomeativo = 'PETR4.SA'
datainicio = '2022-01-01' # YYYY-MM-DD
datafim = '2023-01-01' # YYYY-MM-DD
diretorio = 'C:\Temp\Python_YT\Arquivo_Exemplo\Ativos'
arquivo = 'petrobras.csv'

# %% 

################################################################################################

# Etapa 04 - Processo de Extração

# Processo de Extração - MODULO 01
# Usando Apenas UM Ativo

dfYF = web.get_data_yahoo(nomeativo, datainicio, datafim)

dfYF = dfYF.reset_index()

diretorio_arquivo = diretorio + '\\' + arquivo

dfYF.to_csv(diretorio_arquivo,
            sep=',',
            index=False)

# %%

# Processo de Extração - MODULO 02 - Parte 01
# Usando Apenas UM Ativo

estrutura = {'Ativo': ['PETR4.SA'] }

dfParametrizao = pd.DataFrame(estrutura)

for nomeativo in dfParametrizao['Ativo']:

    dfYF = web.get_data_yahoo(nomeativo, datainicio, datafim)

    dfYF = dfYF.reset_index()

    diretorio_arquivo = diretorio + '\\' + nomeativo + '.csv'

    dfYF.to_csv(diretorio_arquivo,
                sep=',',
                index=False)

# %%

# Processo de Extração - MODULO 02 - Parte 02
# Usando Apenas UM Ativo

estrutura = 'C:\Temp\Python_YT\Arquivo_Exemplo\Ativos\\ativo_parametro.csv'

dfParametrizao = pd.read_csv(estrutura)

for nomeativo in dfParametrizao['Ativo']:

    dfYF = web.get_data_yahoo(nomeativo, datainicio, datafim)

    dfYF = dfYF.reset_index()

    diretorio_arquivo = diretorio + '\\' + nomeativo + '.csv'

    dfYF.to_csv(diretorio_arquivo,
                sep=',',
                index=False)
    
# %%

# Processo de Extração - MODULO 03
# Usando + de UM Ativo

estrutura = 'C:\Temp\Python_YT\Arquivo_Exemplo\Ativos\\ativo_parametro.csv'

dfParametrizao = pd.read_csv(estrutura)

dfUnificado = pd.DataFrame()

for nomeativo in dfParametrizao['Ativo']:
    
    dfYF = web.get_data_yahoo(nomeativo, datainicio, datafim)

    dfYF = dfYF.reset_index()

    dfUnificado = dfUnificado.append(dfYF)

diretorio_arquivo = diretorio + '\\ativo_unificado.csv'

dfUnificado.to_csv(diretorio_arquivo,
            sep=',',
            index=False)

# %% 

################################################################################################

# Processo de Extração - MODULO 03
# Usando + de UM Ativo
# Criando uma funlção no python

def extracao_api_yahoo_finance(estrutura, diretorio, arquivo, datainicio, datafim):

    dfParametrizao = pd.read_csv(estrutura)

    dfUnificado = pd.DataFrame()

    for nomeativo in dfParametrizao['Ativo']:
        
        dfYF = web.get_data_yahoo(nomeativo, datainicio, datafim)

        dfYF = dfYF.reset_index()

        dfYF['NomeAtivo'] = nomeativo

        dfYF['DataExtracao'] = datetime.now()

        dfUnificado = dfUnificado.append(dfYF)

    diretorio_arquivo = diretorio + '\\' + arquivo

    dfUnificado.to_csv(diretorio_arquivo,
                sep=',',
                index=False)

# %% 

estrutura = 'C:\Temp\Python_YT\Arquivo_Exemplo\Ativos\\ativo_parametro.csv'
diretorio = 'C:\Temp\Python_YT\Arquivo_Exemplo\Ativos'
arquivo = 'ativo_unificado.csv'
datainicio = '2018-01-01'
datafim = '2023-09-01'

extracao_api_yahoo_finance(estrutura, diretorio, arquivo, datainicio, datafim)

# %%

################################################################################################

# Etapa 05 - Ingestão e Manipulação dos Dados Extraídos e Geração de um Arquivo Final
#

arquivo = 'C:\Temp\Python_YT\Arquivo_Exemplo\Ativos\\ativo_unificado.csv'

dfAtivo = pd.read_csv(arquivo
                      ,parse_dates=['Date','DataExtracao'])


dfAtivo = dfAtivo.assign(ANO=dfAtivo['Date'].dt.year
                         ,MES=dfAtivo['Date'].dt.strftime('%m')
                         ,DIA=dfAtivo['Date'].dt.strftime('%d')
                         ,ANOMES=dfAtivo['Date'].dt.strftime('%Y-%m'))


dfAtivo = dfAtivo.rename(columns={
                        'Date' : 'DATA_NEGOCIACAO',
                        'Open' : 'VALOR_ABERTURA',
                        'High' : 'VALOR_MAIOR_NEGOCIACAO',
                        'Low' : 'VALOR_MENOR_NEGOCIACAO',
                        'Close' : 'VALOR_FECHAMENTO',
                        'Adj Close' : 'VALOR_FECHAMENTO_AJUSTADO',
                        'Volume' : 'VOLUME_NEGOCIADO',
                        'DataExtracao' : 'DATA_EXTRACAO',
                        'NomeAtivo' : 'NOME_ATIVO'
                        })

dfAtivo = dfAtivo[['NOME_ATIVO',
'DATA_NEGOCIACAO',
'ANO',
'MES',
'DIA',
'ANOMES',
'VALOR_ABERTURA',
'VALOR_MAIOR_NEGOCIACAO',
'VALOR_MENOR_NEGOCIACAO',
'VALOR_FECHAMENTO',
'VALOR_FECHAMENTO_AJUSTADO',
'VOLUME_NEGOCIADO',
'DATA_EXTRACAO']]

# %%++

diretorio = 'C:\Temp\Python_YT\Arquivo_Exemplo\Ativos'
arquivo = 'ativo_unificado.csv'
diretorio_arquivo = diretorio + '\\' + arquivo

dfAtivo.to_csv(diretorio_arquivo,
                sep=',',
                index=False)