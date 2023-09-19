# %%

# BIBLIOTECAS A SEREM INSTALADAS

#!pip install pyodbc
#!pip install sqlalchemy

# %%

# BIBLIOTECAS A SEREM IMPORTADAS

import pandas as pd
import csv
import pyodbc
import json
from sqlalchemy import create_engine
import numpy as np

# %%

# ARQUIVOS A SEREM IMPORTADOS E GERADOS
# ARQUIVO: VIDEOS YOUTUBE
#FONTE: https://www.kaggle.com/datasets/datasnaek/youtube-new

def importa_arquivo_videos_youtube(arquivo_video_origem, arquivo_video_destino, arquivo_parametro_json):

    # IMPORTAÇÃO DO ARQUIVO BRUTO
    df = pd.read_csv(arquivo_video_origem, header=0)

    # 01.01 - DEFINIÇÃO DAS COLUNAS QUE IREMOS PRECISAR
    dfVideoYouTube = pd.read_csv(arquivo_video_origem
                    ,usecols=[0,2,3,4,7,8,9,10]
                    ,names=['CodVideoYouTube'
                            ,'NomVideo'
                            ,'NomCanal'
                            ,'CodCategoriaVideo'
                            ,'NumVisualizacao'
                            ,'NumLike'
                            ,'NumDislike'
                            ,'NumComentario']
                    ,dtype={'CodVideoYouTube':'str'
                            ,'NomVideo':'str'
                            ,'NomCanal':'str'
                            ,'CodCategoriaVideo':'int32'
                            ,'NumVisualizacao':'int32'
                            ,'NumLike':'int64'
                            ,'NumDislike':'int32'
                            ,'NumComentario':'int32'}
                    ,header=0)


    # 01.02 - GERAÇÃO DO ARQUIVO COM APENAS AS INFORMAÇÕES NECESSÁRIAS
    dfVideoYouTube.to_csv(arquivo_video_destino
            ,sep=';'
            ,index=False)

    # 01.03 - INGESTÃO DOS DADOS PARA O BANCO DE DADOS
    paramJson 	= arquivo_parametro_json
    file 		= open(paramJson)
    dfJson 		= json.load(file)

    for tag in dfJson:
        server 		= dfJson[tag]['server']
        database 	= dfJson[tag]['database']
        username 	= dfJson[tag]['username']
        password 	= dfJson[tag]['password']
        
        
    cnxn 	= pyodbc.connect('DRIVER={SQL Server};SERVER='+server+\
                            ';DATABASE='+database+\
                            ';UID='+username+\
                            ';PWD='+ password)

    cursor 	= cnxn.cursor()

    cursor.execute('''
            IF EXISTS (SELECT 1 FROM SYS.TABLES WHERE NAME = 'TB_VIDEOS_YOUTUBE')
            DROP TABLE dbo.TB_VIDEOS_YOUTUBE;            
            CREATE TABLE dbo.TB_VIDEOS_YOUTUBE(
            IdSeqVideoYouTube int not null identity(1,1)       
            ,CodVideoYouTube varchar(200)
            ,NomVideo varchar(2000)
            ,NomCanal  varchar(2000)
            ,CodCategoriaVideo  bigint
            ,NumVisualizacao bigint
            ,NumLike bigint
            ,NumDislike bigint
            ,NumComentario bigint
            )
            ''')

    query = 'INSERT INTO dbo.TB_VIDEOS_YOUTUBE({0}) VALUES ({1})'

    query = query.format(','.join(dfVideoYouTube.columns), ','.join('?' * len(dfVideoYouTube.columns)))        

    cursor.fast_executemany = True    

    cursor.executemany(query, dfVideoYouTube.values.tolist())

    cnxn.commit()

# %%

def importa_arquivo_categoria_videos_youtube(arquivo_categoria_origem, arquivo_categoria_destino, arquivo_parametro_json):    

    ## 02.01 - INGESTÃO DA BASE DE CATEGORIAS

    # INGESTÃO DO ARQUIVO JSON
    arquivo_dados_categoria = arquivo_categoria_origem
    arquivo = open(arquivo_dados_categoria)
    dados_categoria = json.load(arquivo)

    dfCategoria = pd.DataFrame(dados_categoria)

    # SPLIT DA COLUNA (snippet)
    dfCategoria[['channelId', 'title', 'assignable']] = dfCategoria['snippet'].apply(pd.Series)

    # APOS SPLIT E CRIAÇÃO DE NOVAS COLUNAS, DROP COLUNA snippet
    dfCategoria.drop(columns=['snippet'], inplace=True)

    # AJUSTE DO DATATYPE DA COLUNA ID PARA INT
    dfCategoria['id'] = dfCategoria['id'].astype(int)

    # ORDENAÇÃO DO DATAFRAME
    dfCategoria = dfCategoria[['id','title']].sort_values(by='id'
                                                        , ascending=True)

    # RENOMEAÇÃO DAS COLUNAS
    dfCategoria = dfCategoria.rename(columns={'id':'CodCategoriaVideo'
                                            , 'title':'NomCategoriaVideo'})

    # GERAÇÃO DE UMA NOVA BASE
    dfCategoria.to_csv(arquivo_categoria_destino
            ,sep=';'
            ,index=False)

    # 02.02 - INGESTÃO DOS DADOS DE CATEGORIA PARA O BANCO DE DADOS
    paramJson 	= arquivo_parametro_json
    file 		= open(paramJson)
    dfJson 		= json.load(file)

    for tag in dfJson:
        server 		= dfJson[tag]['server']
        database 	= dfJson[tag]['database']
        username 	= dfJson[tag]['username']
        password 	= dfJson[tag]['password']
        
        
    cnxn 	= pyodbc.connect('DRIVER={SQL Server};SERVER='+server+\
                            ';DATABASE='+database+\
                            ';UID='+username+\
                            ';PWD='+ password)

    cursor 	= cnxn.cursor()

    cursor.execute('''
            IF EXISTS (SELECT 1 FROM SYS.TABLES WHERE NAME = 'TB_CATEGORIA_VIDEOS_YOUTUBE')
            DROP TABLE dbo.TB_CATEGORIA_VIDEOS_YOUTUBE;            
            CREATE TABLE dbo.TB_CATEGORIA_VIDEOS_YOUTUBE(
            IdSeqCategoriaVideoYouTube int not null identity(1,1)       
            ,CodCategoriaVideo  int not null
            ,NomCategoriaVideo  varchar(2000)  not null
            )
            ''')

    query = 'INSERT INTO dbo.TB_CATEGORIA_VIDEOS_YOUTUBE({0}) VALUES ({1})'

    query = query.format(','.join(dfCategoria.columns), ','.join('?' * len(dfCategoria.columns)))        

    cursor.fast_executemany = True    

    cursor.executemany(query, dfCategoria.values.tolist())

    cnxn.commit()
# %%

#arquivo_video_origem = 'C:\Temp\Python_YT\Arquivo_Exemplo\Videos\\USvideos.csv'
#arquivo_video_destino = 'C:\Temp\Python_YT\Arquivo_Exemplo\Videos\\videos_youtube.csv'
#arquivo_categoria_origem = 'C:\Temp\Python_YT\Arquivo_Exemplo\Videos\\US_category_id.json'
#arquivo_categoria_destino = 'C:\Temp\Python_YT\Arquivo_Exemplo\Videos\\categoria_videos_youtube.csv'
#arquivo_parametro_json = "c:\Temp\Config\config.json"

#importa_arquivo_videos_youtube(arquivo_video_origem, arquivo_video_destino, arquivo_parametro_json)

#importa_arquivo_categoria_videos_youtube(arquivo_categoria_origem, arquivo_categoria_destino, arquivo_parametro_json)
