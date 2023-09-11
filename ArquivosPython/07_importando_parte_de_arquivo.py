# %%

# Importando Bilbioteca

import pandas as pd

# %%

# Definindo Variáveis

arquivo_origem = 'C:\Temp\Python_YT\Arquivo_Exemplo\precos-gasolina-etanol-06.csv'
arquivo_destino = 'C:\Temp\Python_YT\Arquivo_Exemplo\PRECO_COMBUSTIVEIS.csv'

sep=';'
enconding = 'utf-8'
header=0
colunas_indice = 1,2,8,10,11,12
colunas_nome = ['UF','Municipio','Bairro','Produto','DatadaColeta','ValordeVenda']
dtype={
 'UF':'string'
 ,'Municipio':'string'
 ,'Bairro':'string'
 ,'Produto':'string'
 ,'DatadaColeta':'string'
 ,'ValordeVenda':'string'
}


# %% 

# Criação do Processo de Importação 

df = pd.read_csv(arquivo_origem
                 , sep=sep
                 , encoding=enconding
                 , usecols=colunas_indice
                 , names=colunas_nome
                 , parse_dates=[4]
                 , dtype=dtype
                 , header=header)

df

# %%

# Convertendo coluna para tipo FLOAT

df['ValordeVenda'] = df['ValordeVenda'].str.replace(',','.').astype(float)

# %% 

df.to_csv(arquivo_destino
          , sep=sep
          , index=False )

# %%

df.info()
# %%

df.head(3)

# %%
