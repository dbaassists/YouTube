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
arquivo_parametro_json = "c:\Temp\Config\config_azure.json"

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
## 01 - FILTRANDO VALORES 

df_Exemplo_WHERE =  dfVideoYouTube.groupby('NomCanal', as_index=False).agg(QTD=('NumVisualizacao','count'))

# %%

condicao_01 = df_Exemplo_WHERE['QTD']==1
df_Exemplo_WHERE[condicao_01]

# %% 

df_Exemplo_WHERE.loc[condicao_01]['NomCanal']

# %% 

condicao_02 = ((df_Exemplo_WHERE['QTD']>=1) & (df_Exemplo_WHERE['QTD'] <= 10))
df_Exemplo_WHERE[condicao_02].sort_values(by='QTD')

# %%

condicao_03 = df_Exemplo_WHERE['QTD'].isin([1,10])
df_Exemplo_WHERE[condicao_03]

# %%

df_Exemplo_WHERE.query("QTD >= 1 and QTD <= 10")

# %%


df_Exemplo_WHERE.query("QTD == 1 | QTD == 10")
# %%
