# Projeto 6 - Engenharia Financeira com IA - Estruturação de Derivativos Para Hedging de Riscos de Commodities

# Etapa 2 - Modelagem Estatística

# Imports
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

print("\nSimulador DSA Para Estratégia de Hedge com Modelagem Estatística!")

##### Modelagem Estatística #####

# Definimos a semente (Apenas para reproduzir o projeto. Depois pode ser removido!)
SEED = 142
random.seed(SEED)
np.random.seed(SEED)

# Carrega o arquivo CSV
df = pd.read_csv("preco_petroleo.csv")

# Cria o modelo ARIMA
modelo = ARIMA(df['PrecoPetroleo'], order = (5,1,0))

# Treina o modelo
modelo_dsa = modelo.fit()

# Previsão para os próximos 30 períodos (dias)
# Estamos prevendo o preço do petróleo em um horizonte de 30 dias
output = modelo_dsa.forecast(steps = 30)

# O drift e a volatilidade serão calculados usando as previsões do modelo ARIMA e depois utilizados na Simulação Monte Carlo. 

# Vamos calcular o drift e a volatilidade com base nas previsões do modelo ARIMA
# Calculamos primeiro os retornos previstos
retornos_previstos = np.diff(output) / output[:-1]  

# Plot das previsões do modelo
plt.hist(retornos_previstos, bins = 30, density = True)
plt.title('Previsões do Retorno ao Investir em Petróleo por 30 dias')
plt.xlabel('Retorno Previsto ao Investir em Petróleo')
plt.ylabel('Frequência')
plt.savefig('ME_previsoes_retornos.png')
plt.show()

# A média dos retornos usaremos como drift
drift = np.mean(retornos_previstos) 

# O desvio padrão dos retornos usaremos como volatilidade
volatilidade = np.std(retornos_previstos) 

print("\nDrift previsto com base no modelo estatístico:")
print(drift)
print("\nVolatilidade prevista com base no modelo estatístico:")
print(volatilidade)

##### Simulação de Monte Carlo #####

# Número de simulações
n_simulations = 1000

# Lista para 30 dias de previsões
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
plt.savefig('ME_previsoes_precos_smc.png')
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



