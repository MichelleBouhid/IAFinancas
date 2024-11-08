# Projeto 7 - IA Aplicada a Finanças: Blockchain e IA para Gestão de Empréstimos Pessoais - Clube do Empréstimo

Este projeto integra Inteligência Artificial e Blockchain para a gestão de empréstimos pessoais. A primeira parte aborda a IA para prever a probabilidade de pagamento de empréstimos, enquanto a segunda parte explora a utilização da tecnologia Blockchain para armazenar transações e dados de contratos.

## Estrutura do Projeto

### Etapa 1: Exploração e Pré-processamento de Dados

- **Objetivo**: Preparar os dados para o treinamento do modelo de classificação, garantindo a qualidade e a representatividade das variáveis relevantes para o problema de inadimplência.
- **Conteúdo**:
  - Carregamento dos dados históricos do Lending Club (disponíveis no Kaggle).
  - Análise e remoção de colunas com valores ausentes ou constantes.
  - Filtragem de colunas altamente correlacionadas para evitar redundância e multicolinearidade.
  - Transformação da variável-alvo `loan_status` em `loan_paid` (1 para "Fully Paid" e 0 para "Charged Off").

### Etapa 2: Engenharia de Atributos

- **Objetivo**: Otimizar as variáveis do conjunto de dados para o modelo, utilizando técnicas de codificação e padronização para assegurar a adequação dos dados ao modelo de Rede Neural.
- **Conteúdo**:
  - Tratamento de variáveis categóricas com `One Hot Encoding` e criação de variáveis dummy.
  - Conversão de variáveis contínuas e categóricas, como `term`, `grade` e `sub_grade`, em variáveis numéricas apropriadas.
  - Eliminação de colunas não informativas (e.g., `zip_code`, `addr_state`).
  - Padronização dos dados com `MinMaxScaler` para garantir uma escala uniforme entre as variáveis.

### Etapa 3: Modelagem Preditiva

- **Objetivo**: Desenvolver e treinar um modelo de Rede Neural Artificial para a classificação binária do status de pagamento do empréstimo.
- **Conteúdo**:
  - Separação dos dados em conjuntos de treino (80%) e teste (20%).
  - Implementação de uma Rede Neural com camadas densas, usando Keras e TensorFlow.
  - Funções de ativação `ReLU` nas camadas ocultas e `sigmoid` na camada de saída para fornecer uma probabilidade de pagamento.
  - Treinamento com 40 épocas e batch size de 512, monitorando a acurácia e a perda em treino e validação.

### Etapa 4: Avaliação do Modelo

- **Objetivo**: Avaliar a performance da rede neural em prever corretamente os pagamentos e inadimplências de empréstimos.
- **Conteúdo**:
  - Análise de gráficos de erro e acurácia ao longo das épocas.
  - Avaliação da matriz de confusão e do `classification_report` para precisão e recall.
  - Obtenção de uma acurácia de 99%, com bom desempenho na classificação de mutuários inadimplentes.

### Etapa 5: Previsão para Novo Usuário

- **Objetivo**: Simular a aplicação do modelo com dados de um novo usuário.
- **Conteúdo**:
  - Padronização dos dados do novo usuário com o mesmo `MinMaxScaler` do modelo.
  - Previsão do modelo, retornando 1 para "vai pagar" e 0 para "não vai pagar".

## Tecnologias e Bibliotecas

- **Python 3.9.13**
- **Bibliotecas**:
  - `pandas`, `numpy`, `matplotlib`, `seaborn` - Manipulação e visualização de dados.
  - `tensorflow` e `keras` - Construção da Rede Neural.
  - `sklearn` - Pré-processamento de dados e avaliação do modelo.

## Configuração do Ambiente

Para executar o projeto, instale as bibliotecas listadas abaixo:

```bash
pip install pandas numpy matplotlib seaborn tensorflow sklearn


## Parte 2 - Blockchain

### Objetivo

Utilizar a tecnologia blockchain para armazenar e validar informações de empréstimos, como os dados do usuário, informações do contrato e os resultados do modelo de IA. Através de uma interface web, dados podem ser submetidos e recuperados da rede blockchain, garantindo a segurança e transparência das transações.

### Estrutura e Características do Blockchain

1. **Descentralização**: Em vez de um banco de dados centralizado, o blockchain armazena informações em uma rede descentralizada, aumentando a resiliência e a segurança dos dados.
2. **Imutabilidade**: Uma vez registrados, os dados em um blockchain não podem ser alterados, o que é essencial para registros financeiros e de contratos.
3. **Transparência**: Todos os registros no blockchain são visíveis para os participantes autorizados, promovendo uma auditoria transparente das transações.
4. **Segurança**: O uso de criptografia assegura que apenas os detentores de chaves privadas possam acessar e manipular os dados, garantindo a privacidade e integridade das informações.

### Configuração do Ambiente Blockchain

Instalação e importação dos pacotes necessários para conexão com uma rede blockchain privada utilizando o Ganache.

```python
# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())

# Instalação do pacote Web3 para interação com a rede blockchain
# https://web3py.readthedocs.io/en/stable/
# !pip install -q -U web3

# Importações
import web3
from web3 import Web3

# Exibe as versões dos pacotes
%reload_ext watermark
%watermark -a "Data Science Academy" --iversions


