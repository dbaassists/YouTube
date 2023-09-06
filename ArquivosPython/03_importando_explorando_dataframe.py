# %% 

import pandas as pd
# %%

arquivos = 'C:\Temp\Python_YT\Arquivo_Exemplo\Combustivel\precos-gasolina-etanol-06_VIRGULA.csv'

df = pd.read_csv(arquivos)

# %%

# head() - N primeiras linhas, por default são as 5 primeiras
# tail() - N últimas linhas, por default são as 5 últimas
# sample() - N aleatórias linhas, por default são as 5 

df.sample(5)



# %%

df.info()
