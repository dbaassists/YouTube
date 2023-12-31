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

dfVideoYouTube = pd.read_csv(arquivo_video_destino
                 ,sep=';'
                 ,header=0)

dfVideoYouTube.head(3)

# %%

## 03 - ORDENANDO UM DATAFRAME

## ORDENAÇÃO CRESCENTE  (ORDER BY COLUNA ASC)

dfVideoYouTube.sort_values(by='CodCategoriaVideo', ascending=True)

## ORDENAÇÃO DECRESCENTE (ORDER BY COLUNA DESC)

dfVideoYouTube.sort_values(by='CodCategoriaVideo', ascending=False)

# %%

## AÇÕES REALIZADAS EM UM DATAFRAME:
## FILTRO DE VALORES
## ORDENAÇÃO NA FORMA DECRESCENTE

(dfVideoYouTube[dfVideoYouTube['NomCanal']=='1MILLION Dance Studio']
                .sort_values(by='NumVisualizacao'
                                , ascending=False
                            ))

# %%
