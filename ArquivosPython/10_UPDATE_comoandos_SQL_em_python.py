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

dfVideoYouTube.info()

# %% 

## CRIAÇÃO DO DATAFRAME DO BILHÃO

dfVideoYouTube_AGG = (dfVideoYouTube.groupby(['NomCanal'], as_index=False)
                .agg(TotalVisualizacoes=('NumVisualizacao', 'sum'))
                .sort_values(by='TotalVisualizacoes'
                             , ascending=False))



# %%

dfVideoYouTube_BILHAO = dfVideoYouTube_AGG.query("TotalVisualizacoes >= 1000000000")


# %%

dfVideoYouTube_BILHAO['Classificacao'] = ''

# %% 

# UPDATE MODO 01

#dfVideoYouTube_BILHAO[dfVideoYouTube_BILHAO['TotalVisualizacoes'] < 1010955663]

# 1010955663 <  = 'X1'
dfVideoYouTube_BILHAO.loc[ dfVideoYouTube_BILHAO['TotalVisualizacoes'] < 1010955663, 'Classificacao' ] = 'X1'

# 1010955663 >= AND < 1300000000 = 'X2'
dfVideoYouTube_BILHAO.loc[ (dfVideoYouTube_BILHAO['TotalVisualizacoes'] >= 1010955663) & (dfVideoYouTube_BILHAO['TotalVisualizacoes'] < 1300000000), 'Classificacao' ] = 'X2'

# 1300000000 >= AND < 1500000000 = 'X3'
dfVideoYouTube_BILHAO.loc[ (dfVideoYouTube_BILHAO['TotalVisualizacoes'] >= 1300000000)& (dfVideoYouTube_BILHAO['TotalVisualizacoes'] < 1500000000) , 'Classificacao' ] = 'X3'

# 1500000000 >=  = 'X4'
dfVideoYouTube_BILHAO.loc[ dfVideoYouTube_BILHAO['TotalVisualizacoes'] >= 1500000000, 'Classificacao' ] = 'X4'


# %% 

dfVideoYouTube_BILHAO = dfVideoYouTube_BILHAO.reset_index()

# %%

# UPDATE MODO 02

for  indice, coluna in dfVideoYouTube_BILHAO.iterrows():

    # 1010955663 <  = 'X1'
    if coluna['TotalVisualizacoes'] < 1010955663:

        dfVideoYouTube_BILHAO['Classificacao'][indice] = 'X1'

    # 1010955663 >= AND < 1300000000 = 'X2'
    elif ((coluna['TotalVisualizacoes'] >= 1010955663) & (coluna['TotalVisualizacoes'] < 1300000000)):

        dfVideoYouTube_BILHAO['Classificacao'][indice] = 'X2'

    # 1300000000 >= AND < 1500000000 = 'X3'
    elif ((coluna['TotalVisualizacoes'] >= 1300000000) & (coluna['TotalVisualizacoes'] < 1500000000)):

        dfVideoYouTube_BILHAO['Classificacao'][indice] = 'X3'


    # 1500000000 >=  = 'X4'
    elif coluna['TotalVisualizacoes'] >= 1500000000:

        dfVideoYouTube_BILHAO['Classificacao'][indice] = 'X4'


dfVideoYouTube_BILHAO

# %%

# UPDATE MODO 03

# CONDICOES DE ATUALIZAÇÃO
# 1010955663 <  = 'X1'
# 1010955663 >= AND < 1300000000 = 'X2'
# 1300000000 >= AND < 1500000000 = 'X3'
# 1500000000 >=  = 'X4'

condicao = [
(dfVideoYouTube_BILHAO['TotalVisualizacoes'] < 1010955663)
,((dfVideoYouTube_BILHAO['TotalVisualizacoes'] >= 1010955663) & (dfVideoYouTube_BILHAO['TotalVisualizacoes'] < 1300000000))
,((dfVideoYouTube_BILHAO['TotalVisualizacoes'] >= 1300000000) & (dfVideoYouTube_BILHAO['TotalVisualizacoes'] < 1500000000))
,(dfVideoYouTube_BILHAO['TotalVisualizacoes'] >= 1500000000)
]

valor = ['X1','X2','X3','X4']

dfVideoYouTube_BILHAO['Classificacao'] = np.select(condicao , valor)

# %% 

dfVideoYouTube_BILHAO

# %%
