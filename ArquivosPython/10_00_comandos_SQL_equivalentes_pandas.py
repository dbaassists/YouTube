# %%

import pandas as pd
import pyodbc
import numpy as np

pd.options.display.max_rows = 999
pd.options.display.max_columns=999

# %%

arquivo_video_origem = 'C:\Temp\Python_YT\Arquivo_Exemplo\Videos\\videos_youtube.csv'

dfVideoYouTube = pd.read_csv(arquivo_video_origem
                 ,sep=';'
                 ,header=0)

dfVideoYouTube.head(3)

# %%

## 1.1 - SELECIONADO COLUNAS DE UM DATAFRAME

df_Exemplo01 = dfVideoYouTube

df_Exemplo01[['CodVideoYouTube', 'NomVideo','CodCategoriaVideo']]

df_Exemplo01.loc[:, ['CodVideoYouTube', 'NomVideo','CodCategoriaVideo']]

# %%

## 1.2 - SELECIONADO VALORES DISTINTOS DE UM DATAFRAME

df_Exemplo01 = dfVideoYouTube

df_Exemplo01.info()

# %%

# DIFERENTE DO QUE OCORRE NO SQL SERVER, O COMANDO DISTINCT NÃO FUNCIONA
# O DISTINCT NO PANDAS É O COMANDO drop_duplicate()
df_Exemplo01['NomCanal'].distinct

# %% 

df_Exemplo01['NomCanal'].unique()

# %% 

df_Exemplo01_Canal = df_Exemplo01.drop_duplicates(subset=['NomCanal'])

df_Exemplo01_Canal


# %% 

# loc[linhas,colunas]
df_Exemplo01.loc[:, ['NomCanal']].drop_duplicates()
                   
df_Exemplo01['NomCanal'].drop_duplicates()

df_Exemplo01.drop_duplicates(subset=['NomCanal'])

# PODMEOS FAZER DESSA FORMA TBM 
#df_Exemplo01.drop_duplicates(subset=['NomCanal'], inplace=True)
#OU
#df_Exemplo01 = df_Exemplo01.drop_duplicates(subset=['NomCanal'])

#keep=False
#keep='first'
#keep='last'

# default = first
df_Exemplo01.drop_duplicates(subset=['NomCanal'], keep='first')

# %%

## 1.3 - SELECIONANDO N REGISTROS DE UMA TABELA

df_Exemplo01.head(4)
df_Exemplo01.tail(4)
df_Exemplo01.sample(4)

# %%

## 1.4 - USANDO FUNÇÕES DE AGREGAÇÃO

pd.options.display.float_format = "{:.2f}".format

#df_Exemplo01['NumVisualizacao'].describe()

df_Exemplo01.describe()

#df_Exemplo01.describe().T

# %%

df_Exemplo01.agg(NumVisualizacao_MAIOR=( 'NumVisualizacao', 'max')
       ,NumVisualizacao_MENOR=( 'NumVisualizacao', 'min')
       ,NumVisualizacao_QUANTIDADE=( 'NumVisualizacao', 'count')
       ,NumVisualizacao_MEDIA=( 'NumVisualizacao', 'mean')
       ,NumVisualizacao_SOMA=( 'NumVisualizacao', 'sum'))

# %%

df_Exemplo01.agg(NumVisualizacao_MAIOR=( 'NumVisualizacao', 'max')
       ,NumVisualizacao_MENOR=( 'NumVisualizacao', 'min')
       ,NumVisualizacao_QUANTIDADE=( 'NumVisualizacao', 'count')
       ,NumVisualizacao_MEDIA=( 'NumVisualizacao', 'mean')
       ,NumVisualizacao_SOMA=( 'NumVisualizacao', 'sum')).T


# %%

## 02 - FILTRANDO VALORES 

df_Exemplo02 = dfVideoYouTube

dfCanal_QtdVideos = (df_Exemplo02.groupby('NomCanal',as_index=False)
                        .agg(QTD=('NomCanal','count'))
                        .sort_values(by='QTD'))

type(dfCanal_QtdVideos)

dfCanal_QtdVideos.info()

#x = dfCanal_QtdVideos.query("QTD ==2")

#x = dfCanal_QtdVideos.query("QTD >=2 and QTD <= 20")

#x = dfCanal_QtdVideos.query("QTD >=2 & QTD <= 20")

#x = dfCanal_QtdVideos.query("QTD ==2 or QTD == 20")

#x = dfCanal_QtdVideos.query("QTD ==2 | QTD == 20")

#x = dfCanal_QtdVideos.query("QTD in (2 , 20)")

#condicao = [2,20]
#dfCanal_QtdVideos[dfCanal_QtdVideos['QTD'].isin(condicao)]

#dfCanal_QtdVideos[dfCanal_QtdVideos['QTD'] >= 2]
#dfCanal_QtdVideos.loc[dfCanal_QtdVideos['QTD'] >= 2]

#dfCanal_QtdVideos[dfCanal_QtdVideos['QTD'] >= 2]['NomCanal']

#dfCanal_QtdVideos[(dfCanal_QtdVideos['QTD'] >= 2) & (dfCanal_QtdVideos['QTD'] <= 10)]
#dfCanal_QtdVideos.loc[(dfCanal_QtdVideos['QTD'] >= 2) & (dfCanal_QtdVideos['QTD'] <= 10)]

#dfCanal_QtdVideos[dfCanal_QtdVideos['QTD'] == 2].count()
#dfCanal_QtdVideos.loc[dfCanal_QtdVideos['QTD'] == 2].count()

# IR ALTERNANDO A QUANTIDADE
#df.loc[df['NumVisualizacao'] >= 1000000,['NomVideo','NomCanal','NumVisualizacao']]

#df_Exemplo02.loc[(df_Exemplo02['NumVisualizacao'] >= 1000) & (df_Exemplo02['NumVisualizacao'] <= 10000)
#            ,['NomVideo','NomCanal']].drop_duplicates(keep='last')

# %%

## 03 - ORDENANDO UM DATAFRAME

df_Exemplo03 = dfVideoYouTube

#df_Exemplo03.sort_values(by='NumVisualizacao', ascending=True)

#df_Exemplo03.sort_values(by='NumVisualizacao', ascending=False)

# EXPLICAR COMO QUE PODEMOS ORGANIZAR O CÓDIGO
# EXPLICAR A FORMA USANDO \ E ()

df_Exemplo03.loc[df_Exemplo03['NumVisualizacao'] >= 1000000,['NomVideo','NomCanal','NumVisualizacao']].sort_values(by='NumVisualizacao', ascending=False)

df_Exemplo03[df_Exemplo03['NumVisualizacao'] >= 1000000][['NomVideo','NomCanal','NumVisualizacao']].sort_values(by='NumVisualizacao')


# %%

## 04 - AGRUPANDO VALORES 

df_Exemplo04 = dfVideoYouTube

df_Exemplo04.groupby('NomCanal') \
        .agg(QTD_VISUALIZACAO=('NumVisualizacao','count')) \
        .sort_values(by='QTD_VISUALIZACAO')

df_Exemplo04.groupby('NomCanal') \
        .agg(QTD_VISUALIZACAO=('NumVisualizacao','count')) \
        .sort_values(by='QTD_VISUALIZACAO', ascending=False)

# %%

## 05 - COMANDO HAVING 

df_Exemplo05 = dfVideoYouTube

df_Exemplo05 = df_Exemplo05.groupby(['NomCanal'], as_index=False) \
                .agg(QTD_NumVisualizacao=('NumVisualizacao','sum')) \
                .astype({'QTD_NumVisualizacao': 'int'}) \
                .sort_values(by='QTD_NumVisualizacao')

condicao = df_Exemplo05['QTD_NumVisualizacao'] >= 1000000000

df_Exemplo05 = df_Exemplo05.where(condicao).dropna()

df_Exemplo05

# %% 

## 06 - INSERINDO REGISTROS EM UM DATAFRAME

df_Exemplo06 = df_Exemplo05

info_quintellao = pd.DataFrame({'NomCanal': ['Quintellão na Área'],
                        'QTD_NumVisualizacao': [12327]})
df_Exemplo06 = df_Exemplo06.append(info_quintellao, ignore_index=True)

df_Exemplo06


# %%

## 07 - DELETE REGISTROS EM UM DATAFRAME

# (MODO 1 - NÃO OTIMIZADO) PASSANDO O INDICE DO DATAFRAME REFERENTE AO REGISTRO QUE PRETENDEMOS EXCLUIR
# PRECISA CONSULTAR O VALOR DO INDICE E PASSAR PARA O COMANDO DROP

df_Exemplo07 = df_Exemplo06 

print(df_Exemplo07)

df_Exemplo07_01 = df_Exemplo07.drop(labels=[13])

df_Exemplo07_01

# %%

# (MODO 2 - OTIMIZADO)
# NÃO PRECISA CONSULTAR O VALOR DO INDICE E PASSAR PARA O COMANDO DROP
# VOCÊ ESPECIFICA O VALOR QUE DESEJA EXCLUIR, ELE É RETORNADO E PASSADO PARA O DROP

df_Exemplo07 = dfVideoYouTube

indice = np.where(df_Exemplo07['NomCanal'] == '2CELLOS')[0]

print(indice)

#df_Exemplo07_03['NomCanal'].values

#df_Exemplo07_02 = df_Exemplo07.drop(indice)

# %%

dfVideoYouTube[dfVideoYouTube['NomCanal']=='2CELLOS']

# %%

dfVideoYouTube[dfVideoYouTube['NomCanal'].isin(['12 News','2CELLOS'])].index.tolist()


# %% 


#dfVideoYouTube = dfVideoYouTube.sort_index(ascending=True)

df_Exemplo07_03 = dfVideoYouTube

df_Exemplo07_03_TOP_02 = df_Exemplo07_03.groupby(['NomCanal'], as_index=False).agg(QTD=('NomCanal','count')).query('QTD == 2').head(2)

listaExclusao = df_Exemplo07_03[df_Exemplo07_03['NomCanal']==df_Exemplo07_03_TOP_02['NomCanal']].index.tolist()

listaExclusao

# %%

for i in 

    print(canal)
    print(type(canal))

    if canal in df_Exemplo07_03['NomCanal'].values:
        
        df_Exemplo07_03.drop(np.where(df_Exemplo07_03['NomCanal'] == canal)[0], inplace=True)
            
    else:
        print('Nenhum Registro Encontrado!')

        #indice = np.where(df_Exemplo07_03_TOP_02['NomCanal'] == canal)[0]

        #for i in indice.str.split(' '):

        #    print(i)

        #    df_Exemplo07_02 = df_Exemplo07.drop(i)

df_Exemplo07_03[df_Exemplo07_03['NomCanal'].isin(['2CELLOS','12 News'])]

# %%

df_Exemplo07_03[df_Exemplo07_03['NomCanal'].isin(['12 News','2CELLOS'])]

# %%

df_Exemplo07_04.count()




# %%

## 08 - ALTERAR UM DATAFRAME (INCLUINDO UMA NOVA COLUNA)

## 08.01 - INCLUINDO UMA NOVA COLUNA

df_Exemplo08_01 = dfVideoYouTube

df_Exemplo08_01['STATUS'] = bool(0)

df_Exemplo08_01.info()

df_Exemplo08_01.head(3)

# %%

## 08.02 - ELIMINANDO UMA COLUNA DATAFRAME

df_Exemplo08_02 = dfVideoYouTube

del df_Exemplo08_02['STATUS']

df_Exemplo08_02.info()

# %%

## 09 - UPDATE UMA COLUNA DE UM DATAFRAME (ATUALIZANDO VALORES DE ACORDO COM UMA CONDIÇÃO)

df_Exemplo09_01 = df_Exemplo05

df_Exemplo09_01 = df_Exemplo09_01.reset_index()

df_Exemplo09_01['Classificacao'] = ''

df_Exemplo09_01

# %%

for i, coluna in df_Exemplo09_01.iterrows():

    if coluna['QTD_NumVisualizacao'] < 1100000000:
        print(i)

        df_Exemplo09_01['Classificacao'][i] = 'X1'

    elif ((coluna['QTD_NumVisualizacao'] > 1100000000) & (coluna['QTD_NumVisualizacao'] < 1300000000)):
        print(i)

        df_Exemplo09_01['Classificacao'][i] = 'X2'

    elif ((coluna['QTD_NumVisualizacao'] > 1300000000) & (coluna['QTD_NumVisualizacao'] < 1500000000)):
        print(i)

        df_Exemplo09_01['Classificacao'][i] = 'X3'

    else:
        print(i)

        df_Exemplo09_01['Classificacao'][i] = 'X4'                

df_Exemplo09_01

# %%

df_Exemplo09_02 =  df_Exemplo05

df_Exemplo09_02 = df_Exemplo09_02.reset_index()

df_Exemplo09_02['Classificacao'] = ''

df_Exemplo09_02

# %%

df_Exemplo09_02.loc[(df_Exemplo09_02['QTD_NumVisualizacao'] < 1100000000), 'Classificacao'] = 'X1'
df_Exemplo09_02.loc[((df_Exemplo09_02['QTD_NumVisualizacao'] > 1100000000) & (df_Exemplo09_02['QTD_NumVisualizacao'] < 1300000000)), 'Classificacao'] = 'X2'
df_Exemplo09_02.loc[((df_Exemplo09_02['QTD_NumVisualizacao'] > 1300000000) & (df_Exemplo09_02['QTD_NumVisualizacao'] < 1500000000)), 'Classificacao'] = 'X3'
df_Exemplo09_02.loc[((df_Exemplo09_02['QTD_NumVisualizacao'] > 1500000000)), 'Classificacao'] = 'X4'

df_Exemplo09_02

# %%

df_Exemplo09_03 = df_Exemplo05

df_Exemplo09_03 = df_Exemplo09_03.reset_index()

df_Exemplo09_03['Classificacao'] = ''

df_Exemplo09_03

# %%

condicao = [
(df_Exemplo09_03['QTD_NumVisualizacao'] < 1100000000)
,((df_Exemplo09_03['QTD_NumVisualizacao'] > 1100000000) & (df_Exemplo09_03['QTD_NumVisualizacao'] < 1300000000))
,((df_Exemplo09_03['QTD_NumVisualizacao'] > 1300000000) & (df_Exemplo09_03['QTD_NumVisualizacao'] < 1500000000))
,(df_Exemplo09_03['QTD_NumVisualizacao'] > 1500000000)
]

valor = ['X1','X2','X3','X4']

df_Exemplo09_03['Classificacao'] = np.select(condicao, valor, default='X0')

print(df_Exemplo09_03)


# %%

## 10.1 - INNER JOIN

arquivo_categoria_origem = 'C:\Temp\Python_YT\Arquivo_Exemplo\Videos\\categoria_videos_youtube.csv'

dfCategoria = pd.read_csv(arquivo_categoria_origem
                 ,sep=';'
                 ,header=0)
dfCategoria

dfCategoria.info()

# %%

# MODO - 01
dfVideoYouTube.merge(dfCategoria)

# MODO - 02
pd.merge(dfVideoYouTube
         , dfCategoria
         , on='CodCategoriaVideo'
         , how='inner')

# MODO - 03
dfCategoria_02 = dfCategoria.rename(columns={'CodCategoriaVideo':'CodCategoria'})

(pd.merge(dfCategoria_02
                     ,how='inner'
                     ,left_on=['CodCategoriaVideo']
                     ,right_on=['CodCategoria'])
                    )

# %%

dfVideoYouTube[dfVideoYouTube['CodCategoriaVideo']==22].merge(dfCategoria)

dfExemplo10_01 = pd.merge(dfVideoYouTube
         , dfCategoria
         , on='CodCategoriaVideo'
         , how='inner')[['NomVideo','CodCategoriaVideo']]

dfExemplo10_01[dfExemplo10_01['CodCategoriaVideo']==22]

# %%

dfVideoYouTube[dfVideoYouTube['CodCategoriaVideo']==22].merge(dfCategoria)

# %%

dfExemplo10_01 = pd.merge(dfVideoYouTube[['NomVideo','CodCategoriaVideo']]
         , dfCategoria[['CodCategoriaVideo','NomCategoriaVideo']]
         , on='CodCategoriaVideo'
         , how='inner') #[['NomVideo','CodCategoriaVideo','NomCategoriaVideo']]

dfExemplo10_01

#dfExemplo10_01[dfExemplo10_01['CodCategoriaVideo']==22]

# %%

(dfVideoYouTube.merge(dfCategoria,how='inner')[['NomVideo','CodCategoriaVideo']])

# %% 

dfCategoria.info()

dfCategoria_02 = dfCategoria.rename(columns={'CodCategoriaVideo':'CodCategoria'})

dfCategoria.info()

# GERA ERRO
#dfVideoYouTube.merge(dfCategoria_02)

# %%

(dfVideoYouTube.merge(dfCategoria_02
                     ,how='inner'
                     ,left_on=['CodCategoriaVideo']
                     ,right_on=['CodCategoria'])
                    [['NomVideo','NomCategoriaVideo']]
                    )

# %%

(dfVideoYouTube.merge(dfCategoria_02
                     ,how='inner'
                     ,left_on=['CodCategoriaVideo']
                     ,right_on=['CodCategoria'])
                    .groupby(['NomVideo','NomCategoriaVideo'])
                    .agg(TOTAL_NumVisualizacao=('NumVisualizacao','sum')
                         ,TOTAL_NumLike=('NumLike','sum')
                         ,TOTAL_NumDislike=('NumDislike','sum')
                         ,TOTAL_NumComentario=('NumComentario','sum'))
                    .sort_values(by='TOTAL_NumVisualizacao')
                    )

# %%

(dfVideoYouTube.merge(dfCategoria_02
                     ,how='inner'
                     ,left_on=['CodCategoriaVideo']
                     ,right_on=['CodCategoria'])
                    .groupby(['NomCategoriaVideo'])
                    .agg(TOTAL_NumVisualizacao=('NumVisualizacao','sum')
                         ,TOTAL_NumLike=('NumLike','sum')
                         ,TOTAL_NumDislike=('NumDislike','sum')
                         ,TOTAL_NumComentario=('NumComentario','sum'))
                    .sort_values(by='TOTAL_NumVisualizacao', ascending=False)
                    )


# %% 
## 10.2 - LEFT JOIN

info_quintellao = pd.DataFrame({
                        'CodVideoYouTube':['asdq7yiwq'],
                        'NomVideo':['Aprenda SQL'],
                        'NomCanal': ['Quintellão na Área'],
                        'NumVisualizacao': [12327]})
df_Exemplo10_02 = dfVideoYouTube.append(info_quintellao, ignore_index=True)

df_Exemplo10_02

# %% 

(df_Exemplo10_02.merge(dfCategoria
                     ,how='left')).where()

# %%

## 10.3 - RIGHT JOIN

dfVideoYouTube.merge(dfCategoria
                     ,how='right')


# %%

dfVideoYouTube.count()
# %%

dfVideoYouTube['CodCategoriaVideo'].unique()
# %%
