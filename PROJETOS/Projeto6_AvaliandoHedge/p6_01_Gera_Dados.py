# Projeto 6 - Engenharia Financeira com IA - Estruturação de Derivativos Para Hedging de Riscos de Commodities

# Etapa 1 - Geração de Dados

# Imports
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Geração dos dados
np.random.seed(0)

# Número de dias
n = 365  

# Preço inicial por barril de petróleo em dólares
preco_inicial_dsa = 50  

# Volatilidade diária
volatilidade_dsa = 0.1  

# drift_dsa diário
drift_dsa = 0.0002  

# Mudança percentual nos dados
mudanca_preco = np.random.normal(drift_dsa, volatilidade_dsa, n)

# Gera os preços
precos = preco_inicial_dsa * np.exp(np.cumsum(mudanca_preco))

# Cria o dataframe
df_dsa = pd.DataFrame({'PrecoPetroleo': precos})

# Salva em disco
df_dsa.to_csv('preco_petroleo.csv', index = False)

# Plot
plt.plot(df_dsa['PrecoPetroleo'])
plt.title('Preço do Peróleo Durante 365 Dias')
plt.xlabel('Dias')
plt.ylabel('Preço em USD$')
plt.show()