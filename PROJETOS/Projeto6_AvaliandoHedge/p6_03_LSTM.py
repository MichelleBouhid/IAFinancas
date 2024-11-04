# Projeto 6 - Engenharia Financeira com IA - Estruturação de Derivativos Para Hedging de Riscos de Commodities

# Etapa 3 - Inteligência Artificial

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Imports
import random
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

print("\nSimulador DSA Para Estratégia de Hedge com Inteligência Artificial!")

##### Inteligência Artificial #####

# Definimos a semente (Apenas para reproduzir o projeto. Depois pode ser removido!)
SEED = 142
random.seed(SEED)
tf.random.set_seed(SEED)
np.random.seed(SEED)

# Carrega o arquivo CSV
df = pd.read_csv("preco_petroleo.csv")

# Calcula a série de retornos
df['Retornos'] = df['PrecoPetroleo'].pct_change().dropna()

# Padroniza os retornos para treinamento
scaler = MinMaxScaler()
scaled_returns = scaler.fit_transform(df[['Retornos']].dropna())

# Listas de X e y
X, y = [], []

# Cria a estrutura de dados com 30 timesteps e 1 saída
for i in range(30, len(scaled_returns)):
    X.append(scaled_returns[i-30:i, 0])
    y.append(scaled_returns[i, 0])

# Converte para array NyumPy e ajusta o shape
X, y = np.array(X), np.array(y)
X = np.reshape(X, (X.shape[0], X.shape[1], 1))

# Inicializa o modelo
modelo_dsa = Sequential()

# Adiciona as camadas LSTM
modelo_dsa.add(LSTM(units = 50, return_sequences = True, input_shape = (X.shape[1], 1)))
modelo_dsa.add(LSTM(units = 50))

# Camada de saída
modelo_dsa.add(Dense(units = 1))

# Compila o modelo
modelo_dsa.compile(optimizer = 'adam', loss = 'mean_squared_error')

# Treina o modelo
modelo_dsa.fit(X, y, epochs = 50, batch_size = 16)

# Após treinar o modelo fazemos previsões para os próximos 30 dias
retornos_previstos = modelo_dsa.predict(X[-30:]) 

# Despadronizamos os retornos previstos
retornos_previstos = scaler.inverse_transform(retornos_previstos)

# Plot das previsões do modelo
plt.hist(retornos_previstos, bins = 30, density = True)
plt.title('Previsões do Retorno ao Investir em Petróleo por 30 dias')
plt.xlabel('Retorno Previsto ao Investir em Petróleo')
plt.ylabel('Frequência')
plt.savefig('IA_previsoes_retornos.png')
plt.show()

# Calculamos o drift e a volatilidade dos retornos previstos
drift = np.mean(retornos_previstos)
volatilidade = np.std(retornos_previstos)

print("\nDrift previsto com base no modelo de IA:")
print(drift)
print("\nVolatilidade prevista com base no modelo de IA:")
print(volatilidade)

##### Simulação de Monte Carlo #####

# Número de simulações
n_simulations = 1000

# Lista
forecast_30d = []

# Inicia um loop para realizar 'n_simulations' simulações.
for _ in range(n_simulations):
    
    # Inicia uma lista com o último preço de petróleo observado.
    precos_simulados = [df['PrecoPetroleo'].iloc[-1]]
    
    # Inicia um loop para simular preços durante 30 dias.
    for i in range(30):
        
        # Calcula um novo preço simulado usando o último preço, o drift e a volatilidade.
        preco_simulado = precos_simulados[-1] * np.exp(random.gauss(drift, volatilidade))
        
        # Adiciona o novo preço simulado à lista de preços simulados.
        precos_simulados.append(preco_simulado)
    
    # Adiciona o último preço simulado à lista 'forecast_30d' que guarda as simulações.
    forecast_30d.append(precos_simulados[-1])

# Plot do forecast_30d
plt.hist(forecast_30d, bins = 50, density = True)
plt.title('Simulação Monte Carlo Para os Preços do Petróleo em 30 dias')
plt.xlabel('Preço')
plt.ylabel('Frequência')
plt.savefig('IA_previsoes_preco_smc.png')
plt.show()

##### Estratégia de Hedge #####

# Custo corrente do petróleo é o último valor da série de dados
custo_corrente_petroleo = 1.5 * df['PrecoPetroleo'].iloc[-1]

# O custo futuro do petróleo é a média das simulações de 30 dias multiplicada pelo fator 1.5
custo_futuro_petroleo = 1.5 * np.mean(forecast_30d)

# Suponha que você consome 1000 barris por dia
consumo_diario = 1000  

# Custo futuro sem hedge
custo_futuro_sem_hedge = custo_futuro_petroleo * consumo_diario * 30

# Suponha que o contrato de futuros permite que você fixe o preço do petróleo em $35
preco_contrato_futuro = 45

# Calculamos o custo futuro considerando o instrumento financeiro (contrato futuro)
custo_futuro_petroleo_com_hedge = 1.5 * preco_contrato_futuro

# Custo futuro com estratégia de Hedge. Estamos reduzindo o risco, pois temos o preço do petróleo fixado através de um instrumento financeiro
custo_futuro_com_hedge = custo_futuro_petroleo_com_hedge * consumo_diario * 30

print(f"\nCusto futuro sem hedge: ${custo_futuro_sem_hedge}")
print(f"\nCusto futuro com hedge: ${custo_futuro_com_hedge}")

# Verifica o resultado e imprime a conclusão
if custo_futuro_com_hedge < custo_futuro_sem_hedge:
    print("\nA estratégia de Hedge resultou em economia.")
else:
    print("\nA estratégia de Hedge não resultou em economia.")

print("\nFim\n")




