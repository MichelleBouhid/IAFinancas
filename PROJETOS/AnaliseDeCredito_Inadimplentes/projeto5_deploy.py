# Projeto 5 - IA Para Prever Inadimplência com Base no Histórico de Crédito

# Imports
import pandas as pd
import torch
import torch.nn as nn
from joblib import load
import warnings
warnings.filterwarnings('ignore')

# Definição da arquitetura do modelo (deve ser a mesma que foi treinada)
class ModeloNN(nn.Module):
    def __init__(self, input_dim):
        super(ModeloNN, self).__init__()
        self.fc1 = nn.Linear(input_dim, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 32)
        self.fc4 = nn.Linear(32, 1)
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        x = self.sigmoid(self.fc4(x))
        return x

# Carregar os dados de entrada
data = pd.read_csv('dados/novos_clientes.csv')

# Carregar o scaler
scaler = load('modelos/dsa_scaler.pkl')

# Aplicar a transformação do scaler nos novos dados
X_new = scaler.transform(data)

# Converter os dados transformados para tensores PyTorch
X_new_tensor = torch.FloatTensor(X_new)

# Definir a arquitetura do modelo
model = ModeloNN(X_new.shape[1])

# Carregar o modelo treinado
model.load_state_dict(torch.load('modelos/dsa_modelo.pth'))

# Definir o modelo como modo de avaliação (importante para desativar camadas como Dropout, se existirem)
model.eval()

# Realizar as previsões
with torch.no_grad():  # desativar o cálculo do gradiente para melhorar a performance
    probabilities = model(X_new_tensor)
    
# Convertendo as probabilidades para classes com base no limiar de 0.5
predicted_classes = (probabilities > 0.5).int().numpy()

print('\nPrevisões Feitas Pelo Modelo de IA:\n')

# Loop para imprimir a previsão para cada cliente
for idx, prediction in enumerate(predicted_classes):
    if prediction == 0:
        print(f'Este cliente: {data.iloc[idx].to_dict()} provavelmente não será inadimplente.')
    else:
        print(f'Este cliente: {data.iloc[idx].to_dict()} provavelmente será inadimplente.')

# Criar um DataFrame para armazenar os resultados
results = []

# Loop para coletar a previsão para cada cliente
for idx, prediction in enumerate(predicted_classes):
    client_data = data.iloc[idx].to_dict()
    client_data["Previsão"] = "provavelmente não será inadimplente" if prediction == 0 else "provavelmente será inadimplente"
    results.append(client_data)

# Converter a lista de dicionários em um DataFrame
results_df = pd.DataFrame(results)

print('\nPrevisões Salvas em Disco em resultados/resultados_previsoes.csv!\n')

# Salvar o DataFrame em um arquivo CSV
results_df.to_csv("resultados/resultados_previsoes.csv", index=False)



