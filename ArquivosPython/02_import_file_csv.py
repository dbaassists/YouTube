# %% 

# importar as bibliotecas
import pandas as pd
from glob import glob

# %% 

# criar o processo de importação para UM ÚNICO arquivo

path = 'C:\Temp\Python_YT\Arquivo_Exemplo\Arquivos_Candidatos\consulta_cand_2022_AC.csv'

df = pd.read_csv(path
                ,encoding='latin-1'
                ,sep=';')

# %%

# visualizar o nosso dataframe
df['SG_UF'].unique()

# %% 

# criar o processo de importação para VÁRIOS arquivo

path_todos = 'C:\Temp\Python_YT\Arquivo_Exemplo\Arquivos_Candidatos\consulta_cand_2022_*.csv'

lista_arquivos = sorted(glob(path_todos))

dfArquivoCandidato = pd.DataFrame()

for arquivo_importacao in lista_arquivos: 

    df = pd.read_csv(arquivo_importacao
                ,encoding='latin-1'
                ,sep=';')
    
    dfArquivoCandidato = dfArquivoCandidato.append(df)


# %%

dfArquivoCandidato['SG_UF'].unique()
