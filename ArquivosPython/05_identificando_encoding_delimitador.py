# %% 

# Importar bibliotecas

import pandas as pd
import bibliotecas

# %%

def detecta_encoding(arquivo):

    with open(arquivo, 'rb') as arquivo_encoding:

        resultado_encoding = chardet.detect(arquivo_encoding.read())

        enconding_detectado = resultado_encoding['encoding']

    return enconding_detectado

#df.head()

# %% 

# Detectar o Delimitador

def detecta_delimitador(arquivo):

    with open(arquivo, 'r', newline='') as arquivo_delimitador:

        detector_delimitador = csv.Sniffer()

        amostra_delimitador = arquivo_delimitador.read(1024)

        delimitador_detectado = detector_delimitador.sniff(amostra_delimitador).delimiter

    return delimitador_detectado

# %% 

arquivo = 'C:\Temp\Python_YT\Arquivo_Exemplo\Arquivos_Candidatos\consulta_cand_2022_AC.csv'

enconding_detectado = bibliotecas.detecta_encoding(arquivo)
delimitador_detectado = bibliotecas.detecta_delimitador(arquivo)

df = pd.read_csv(arquivo
                 , encoding=enconding_detectado
                 , sep=delimitador_detectado)


df
# %%
