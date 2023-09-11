# %%

# 1 Etapa - Importar Biblioteca

import pandas as pd

# %% 

# 2 Etapa - Definir Variáveis

palavra = 'JOSÉ'

letras_de =     'áéíóúàèìòùâêîôûãõäëïöüçñÿýÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕÄËÏÖÜÇÑŸÝ'
letras_para =   'aeiouaeiouaeiouaoaeioucnyyAEIOUAEIOUAEIOUAOAEIOUCNYY'
palavra_retorno = ''
contador = 0


# %% 

# 3 Etapa - Criação do Processo de Remoção de Acentuação

def remove_acentuacao(palavra):
    
    letras_de =     'áéíóúàèìòùâêîôûãõäëïöüçñÿýÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕÄËÏÖÜÇÑŸÝ'
    letras_para =   'aeiouaeiouaeiouaoaeioucnyyAEIOUAEIOUAEIOUAOAEIOUCNYY'
    palavra_retorno = ''
    contador = 0

    while contador < len(palavra):

        letra = palavra[contador]
        contador += 1
        indice = letras_de.find(letra)

        if indice == -1:
            palavra_retorno += letra

        else:
            palavra_retorno += letras_para[indice]

    return palavra_retorno
    

# %%

palavra = 'JOSÉ'
remove_acentuacao(palavra)

# %% 

# Etapa 4 - Importando os Dados

arquivo = 'C:\Temp\Python_YT\Arquivo_Exemplo\\alunos_acentuacao.csv'

df = pd.read_csv(arquivo, sep=';')

for i in df.index:

    df['Aluno'][i] = remove_acentuacao(df['Aluno'][i])
 
df

