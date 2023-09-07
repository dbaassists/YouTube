# %%
# importando as bibliotecas

import os
import zipfile

# %%

# definir os diretorio de origem e destino

diretorio_origem = 'C:\Temp\Python_YT\Download_File'

diretorio_destino = 'C:\Temp\Python_YT\Arquivo_Exemplo\Arquivos_Candidatos'

# %%

# processo de descompactação do arquivo zip

for arquivo_zip in os.listdir(diretorio_origem):

    #print(arquivo_zip)

    if (os.path.splitext(arquivo_zip)[1]=='.zip'):

        #print(arquivo_zip)

        with zipfile.ZipFile(f'{diretorio_origem}\{arquivo_zip}', 'r') as zip_files:

            zip_files.extractall(path=diretorio_destino)