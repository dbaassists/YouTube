# %%

# Importação de Bibliotecas
import pandas as pd
import pyodbc
import numpy as np
from preparacao_ambiente import importa_arquivo_videos_youtube, importa_arquivo_categoria_videos_youtube

# Configurações de Display 
pd.options.display.max_rows = 999
pd.options.display.max_columns=999
pd.options.display.float_format = "{:.2f}".format

# %% 

# 99 - PREPARACAO DO AMBIENTE

# ARQUIVOS DE VIDEOS YOUTUBE
arquivo_video_origem = 'C:\Temp\Python_YT\Arquivo_Exemplo\Videos\\USvideos.csv'
arquivo_video_destino = 'C:\Temp\Python_YT\Arquivo_Exemplo\Videos\\videos_youtube.csv'

# ARQUIVOS DE CATEGORIA
arquivo_categoria_origem = 'C:\Temp\Python_YT\Arquivo_Exemplo\Videos\\US_category_id.json'
arquivo_categoria_destino = 'C:\Temp\Python_YT\Arquivo_Exemplo\Videos\\categoria_videos_youtube.csv'

arquivo_parametro_json = "c:\Temp\Config\config_onpremise.json"

# %%

importa_arquivo_videos_youtube(arquivo_video_origem
              , arquivo_video_destino
              , arquivo_parametro_json)

# %%

importa_arquivo_categoria_videos_youtube(arquivo_categoria_origem,
                                          arquivo_categoria_destino
                                          , arquivo_parametro_json)


# %%

dfVideoYouTube = pd.read_csv(arquivo_video_destino
                 ,sep=';'
                 ,header=0)

dfVideoYouTube.info()

# %% 

dfCategoria = pd.read_csv(arquivo_categoria_destino
                 ,sep=';'
                 ,header=0)

dfCategoria.info()

# %% 

## 01 - RELACIONAMENTOS - INNER JOIN 

# MODO 01

dfVideoYouTube.merge(dfCategoria).head(3)

# %% 

# MODO 02 

pd.merge(
dfVideoYouTube
,dfCategoria
,on='CodCategoriaVideo'
,how='inner'
).head(3)

# %%

# MODO 03

#dfCategoria_ALTERADO = dfCategoria.rename(columns={'CodCategoriaVideo':'CodCategoria'})
#dfCategoria_ALTERADO.info()

#dfVideoYouTube.merge(dfCategoria_ALTERADO).head(3)

colunas = ['NomCanal','NomVideo','NomCategoriaVideo']

dfVideosCategoria = pd.merge(
dfVideoYouTube[['NomCanal','NomVideo','CodCategoriaVideo']]
,dfCategoria_ALTERADO[['CodCategoria','NomCategoriaVideo']]
,left_on='CodCategoriaVideo'
,right_on='CodCategoria'
,how='inner'
)[colunas]

# %% 

dfVideoYouTube.groupby("CodCategoriaVideo").agg(QTD_VIDEOS=('CodCategoriaVideo','count')).sort_values(by='QTD_VIDEOS', ascending=False)

# %% 

dfCategoria.query('CodCategoriaVideo==43')

# %% 

## 02 - RELACIONAMENTOS - LEFT JOIN 

informacao_canal_quintellao = pd.DataFrame(
{
'CodVideoYouTube': ['aksdhaskd', 'lckjlvkjldsk']
,'NomVideo':['Aprenda SQL', 'Aprenda Python']
,'NomCanal':['Quintellão na Área','Quintellão na Área']
,'NumVisualizacao':[2,3]
}    
)

dfVideoYouTube = dfVideoYouTube.append(informacao_canal_quintellao, ignore_index=False)

dfVideoYouTube.query("NomCanal=='Quintellão na Área'")

# %% 

dfVideoYouTube.merge(dfCategoria
                    ,how='left').query("CodCategoriaVideo.isnull()")

# %%

dfVideoYouTube.merge(dfCategoria
                    ,how='left').query("CodCategoriaVideo.notnull()")

# %%

dfVideoYouTube.info()


# %% 

## 03 - RELACIONAMENTOS - RIGHT JOIN 


dfVideoYouTube.merge(dfCategoria
                    ,how='right').count()


# %%

dfVideoYouTube.merge(dfCategoria
                    ,how='right')[['CodVideoYouTube','CodCategoriaVideo','NomCategoriaVideo']].query("CodVideoYouTube.isnull()")

