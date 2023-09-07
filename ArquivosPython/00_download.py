# %%
# Importar as bibliotecas

import os
import requests

# %% 

# Definir o local das nossas fontes de dados (Serão 2)

link = ['https://cdn.tse.jus.br/estatistica/sead/odsele/consulta_cand/consulta_cand_2022.zip', 'http://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv']

# %%

# Criar o diretório de destino dos arquivos

os.makedirs('C:\Temp\Python_YT\Download_File')

# %%

# Criar o processo de ingestão 

for path in link:

    if path == 'https://cdn.tse.jus.br/estatistica/sead/odsele/consulta_cand/consulta_cand_2022.zip':
        
        nome_arquivo = 'consulta_cand_2022.zip'
        
    elif path == 'http://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv':

        nome_arquivo = 'BaseDPEvolucaoMensalCisp.csv'

    diretorio_download = f'C:\Temp\Python_YT\Download_File\{nome_arquivo}'

    print(path)
    print(nome_arquivo)
    print(diretorio_download)

    response = requests.get(path)

    with open(diretorio_download, 'wb') as arquivo_local_download:
        arquivo_local_download.write(response.content)

