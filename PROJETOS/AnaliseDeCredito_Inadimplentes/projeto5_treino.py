# Projeto 5 - IA Para Prever Inadimplência com Base no Histórico de Crédito

# Imports
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from joblib import dump

# Carregar o arquivo CSV
df = pd.read_csv("dados/clientes.csv")

# Separar os dados em treinamento e teste
X = df[['idade', 'salario', 'historico_credito', 'emprestimos_ativos']].values
y = df['inadimplente'].values

# Dividir em dados de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

# Pré-processar os dados (normalização)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Ajustar o tipo e shape dos dados
X_train = torch.FloatTensor(X_train)
y_train = torch.FloatTensor(y_train).unsqueeze(1)
X_test = torch.FloatTensor(X_test)
y_test = torch.FloatTensor(y_test).unsqueeze(1)

# Construir a arquitetura do modelo de Deep Learning
# Deep Learning Book
# https://www.deeplearningbook.com.br/

# Define a classe ModeloNN herdando de nn.Module
class ModeloNN(nn.Module):

    # Método construtor para inicializar a classe
    def __init__(self, input_dim):

        # Chama o construtor da classe pai (nn.Module)
        super(ModeloNN, self).__init__()
        
        # Define a primeira camada totalmente conectada (entrada: input_dim, saída: 128)
        self.fc1 = nn.Linear(input_dim, 128)
        
        # Define a segunda camada totalmente conectada (entrada: 128, saída: 64)
        self.fc2 = nn.Linear(128, 64)
        
        # Define a terceira camada totalmente conectada (entrada: 64, saída: 32)
        self.fc3 = nn.Linear(64, 32)
        
        # Define a quarta camada totalmente conectada (entrada: 32, saída: 1)
        self.fc4 = nn.Linear(32, 1)
        
        # Define a função de ativação Sigmóide
        self.sigmoid = nn.Sigmoid()
    
    # Método forward para propagação para frente da rede
    def forward(self, x):

        # Aplica ReLU após a primeira camada totalmente conectada
        x = torch.relu(self.fc1(x))
        
        # Aplica ReLU após a segunda camada totalmente conectada
        x = torch.relu(self.fc2(x))
        
        # Aplica ReLU após a terceira camada totalmente conectada
        x = torch.relu(self.fc3(x))
        
        # Aplica Sigmóide após a quarta camada totalmente conectada
        x = self.sigmoid(self.fc4(x))
        
        # Retorna a saída
        return x

# Criar o modelo
model = ModeloNN(X_train.shape[1])

# Definir a função de erro
criterion = nn.BCELoss() 

# Definir o otimizador
optimizer = optim.Adam(model.parameters(), lr = 0.001)

print('\nIniciando o Treinamento...\n')

# Treinar o modelo com dados de treino
epochs = 100

# Inicia o loop de treinamento para o número especificado de épocas
for epoch in range(epochs):

    # Zera os gradientes do otimizador para não acumular entre as épocas
    optimizer.zero_grad()
    
    # Realiza a propagação para frente: calcula as previsões do modelo para os dados de treinamento
    outputs = model(X_train)
    
    # Calcula a perda (erro) usando a função de perda especificada (criterion)
    loss = criterion(outputs, y_train)
    
    # Realiza a propagação para trás: calcula os gradientes da perda em relação aos parâmetros do modelo
    loss.backward()
    
    # Atualiza os parâmetros do modelo usando o otimizador
    optimizer.step()
    
    # Imprime informações sobre a época atual e a perda
    print(f'Epoch {epoch+1}/{epochs}, Erro em Treino: {loss.item()}')


# Testar o modelo com dados de teste

# Desativa o cálculo automático de gradientes para melhorar a eficiência durante a inferência
with torch.no_grad():
    
    # Realiza a propagação para frente no conjunto de teste para obter as previsões do modelo
    test_outputs = model(X_test)
    
    # Calcula a perda (erro) no conjunto de teste usando a função de perda (criterion)
    test_loss = criterion(test_outputs, y_test)


print('\nTreinamento Concluído com Sucesso!\n')

print(f'Erro em Teste: {test_loss.item()}')

print('\nModelos Salvos em Disco!\n')

# Salvar o scaler
dump(scaler, 'modelos/dsa_scaler.pkl')

# Salvar o modelo
torch.save(model.state_dict(), 'modelos/dsa_modelo.pth')






