# %%

# Importação de Bibliotecas
import pandas as pd
import pyodbc
import numpy as np
from preparacao_ambiente import importa_arquivo_videos_youtube 

# Configurações de Display 
pd.options.display.max_rows = 999
pd.options.display.max_columns=999
pd.options.display.float_format = "{:.2f}".format

# %% 

# 99 - PREPARACAO DO AMBIENTE

arquivo_video_origem = 'C:\Temp\Python_YT\Arquivo_Exemplo\Videos\\USvideos.csv'
arquivo_video_destino = 'C:\Temp\Python_YT\Arquivo_Exemplo\Videos\\videos_youtube.csv'
arquivo_parametro_json = "c:\Temp\Config\config_onpremise.json"

importa_arquivo_videos_youtube(arquivo_video_origem
              , arquivo_video_destino
              , arquivo_parametro_json)

# %%

## 01 - CRIANDO O DATAFRAME

dfVideoYouTube = pd.read_csv(arquivo_video_destino
                 ,sep=';'
                 ,header=0)

dfVideoYouTube.info()

# %% 

## 02 - AGRUPANDO OS VALORES E GERANDO UM NOVO DATAFRAME

dfVideoYouTube_AGG = dfVideoYouTube.groupby(['NomCanal'], as_index=False).agg(NumVisualizacao=('NumVisualizacao','sum'))

dfVideoYouTube_AGG = dfVideoYouTube_AGG.query("NumVisualizacao >= 1000000000")

informacao_canal_quintellao = pd.DataFrame({'NomCanal': ['Quintellão na Área','Canal XPTO Big Data']
                                            ,'NumVisualizacao':[12327, 21391203]})

dfVideoYouTube_AGG = dfVideoYouTube_AGG.append(informacao_canal_quintellao, ignore_index=True)

## 03 - VISUALIZANDO O DATAFRAME DO BILHÃO

dfVideoYouTube_AGG

# %%

## 04 - DELETE REGISTROS EM UM DATAFRAME (MODO 01 - NÃO OTIMIZADO)

dfVideoYouTube_AGG_01 = dfVideoYouTube_AGG.drop(labels=[13])

dfVideoYouTube_AGG_01.info()

# %% 

## 04 - DELETE REGISTROS EM UM DATAFRAME (MODO 02 - OTIMIZADO)

# ibighit

condicao_exclusao = np.where(dfVideoYouTube_AGG['NomCanal'] == 'ibighit')[0]

dfVideoYouTube_AGG_02 = dfVideoYouTube_AGG.drop(condicao_exclusao)

dfVideoYouTube_AGG_02

# %%
