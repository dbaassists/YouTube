# %% 

# Importar bibliotecas

import pandas as pd
import bibliotecas

# %% 

arquivo = 'C:\Temp\Python_YT\Arquivo_Exemplo\Arquivos_Candidatos\consulta_cand_2022_AC.csv'

enconding_detectado = bibliotecas.detecta_encoding(arquivo)
delimitador_detectado = bibliotecas.detecta_delimitador(arquivo)

df = pd.read_csv(arquivo
                 , encoding=enconding_detectado
                 , sep=delimitador_detectado)


df
# %%
