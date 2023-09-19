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
arquivo_parametro_json = "c:\Temp\Config\config.json"

importa_arquivo_videos_youtube(arquivo_video_origem
              , arquivo_video_destino
              , arquivo_parametro_json)


# %%

# 00 - Importação do Arquivo - DADOS DE VIDEOS YOUTUBE

arquivo_video_origem = 'C:\Temp\Python_YT\Arquivo_Exemplo\Videos\\videos_youtube.csv'

dfVideoYouTube = pd.read_csv(arquivo_video_origem
                 ,sep=';'
                 ,header=0)

dfVideoYouTube.info()

# %% 
## 1.1 - SELECIONADO COLUNAS DE UM DATAFRAME


colunas = ['CodVideoYouTube','NomVideo']
dfVideoYouTube[colunas]

# %% 

dfVideoYouTube.loc[: , colunas]

# %%
## 1.2 - SELECIONADO VALORES DISTINTOS DE UM DATAFRAME

dfVideoYouTube['NomCanal'].unique()

# %% 

dfVideoYouTube.info()

dfVideoYouTube.drop_duplicates()

dfVideoYouTube['NomCanal'].drop_duplicates()

# False
# first
# last

dfVideoYouTube.drop_duplicates(subset=['NomCanal'] , keep='last').count()

# %%
## 1.3 - SELECIONANDO N REGISTROS DE UMA TABELA

dfVideoYouTube.head(5)

dfVideoYouTube.tail(5)

dfVideoYouTube.sample(5)

# %%
## 1.4 - USANDO FUNÇÕES DE AGREGAÇÃO

dfVideoYouTube.describe().T

# %%
