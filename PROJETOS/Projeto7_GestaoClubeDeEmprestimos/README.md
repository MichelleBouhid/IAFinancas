# Projeto 7 - IA Aplicada a Finanças: Blockchain e IA para Gestão de Empréstimos Pessoais - Clube do Empréstimo

Este projeto integra Inteligência Artificial e Blockchain para a gestão de empréstimos pessoais. A primeira parte aborda a IA para prever a probabilidade de pagamento de empréstimos, enquanto a segunda parte explora a utilização da tecnologia Blockchain para armazenar transações e dados de contratos.

# Parte 1 - IA para Gestão de Empréstimos

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


# Parte 2 - Blockchain 


## Estrutura do Projeto

### Etapa 1: Configuração e Instalação de Pacotes

- **Objetivo**: Preparar o ambiente para a criação e execução de contratos inteligentes em uma rede Blockchain simulada.
- **Conteúdo**:
  - Verificação da versão do Python utilizada.
  - Instalação e importação do pacote `web3` para interação com a rede Blockchain.
  - Verificação das versões dos pacotes necessários para o Jupyter Notebook.
- **Ferramenta de Blockchain**: Utilização do Ganache, uma rede Blockchain simulada para desenvolvimento e testes.

### Etapa 2: Conexão com a Rede Blockchain

- **Objetivo**: Estabelecer uma conexão com a rede Blockchain e preparar os dados do contrato inteligente para execução.
- **Conteúdo**:
  - Conexão com o Ganache usando o `HTTPProvider` do Web3.
  - Definição da `ABI` (Application Binary Interface) e do `BYTECODE` do contrato inteligente.
  - Configuração de uma conta padrão para enviar transações.

### Etapa 3: Criação e Execução do Contrato Inteligente

- **Objetivo**: Criar e enviar uma transação de contrato inteligente para a rede Blockchain.
- **Conteúdo**:
  - Criação de um contrato inteligente para armazenar informações relevantes, como dados do empréstimo e estado do pagamento.
  - Geração de uma transação e assinatura com chave privada (obtida pelo Ganache).
  - Envio da transação para a rede Blockchain e obtenção de um recibo de confirmação.

### Características dos Contratos Inteligentes no Contexto de Blockchain

Os contratos inteligentes são scripts de código que executam automaticamente uma ação quando as condições programadas são atendidas. Neste projeto, um contrato inteligente pode:
  - Registrar dados de um novo empréstimo.
  - Armazenar o resultado de análises de IA, como a probabilidade de inadimplência do cliente.
  - Garantir a transparência e segurança na confirmação do empréstimo aprovado ou negado.

### Pontos de Atenção e Ajustes Necessários

O desenvolvimento de um contrato inteligente funcional e seguro requer atenção aos seguintes pontos:
  - **Validação de Dados**: Garantir que os dados inseridos, como o resultado do modelo de IA, estejam corretos e sejam validados no momento do envio para o contrato.
  - **Custos de Transação (Gas Fees)**: No ambiente real de Ethereum, é importante considerar os custos para evitar transações falhas devido à falta de saldo para pagar o "gas".
  - **Segurança das Chaves Privadas**: Manter as chaves privadas protegidas e fora do código público, utilizando variáveis de ambiente ou cofres seguros.

Este projeto representa uma introdução prática ao uso de Blockchain e contratos inteligentes para o gerenciamento de empréstimos pessoais, proporcionando transparência, segurança e auditabilidade nas operações financeiras. A tecnologia Blockchain, combinada com a IA, permite criar uma camada adicional de confiança, especialmente importante no contexto financeiro.

## Tecnologias Utilizadas

- **Blockchain**: Ganache (simulação de rede Ethereum para desenvolvimento local).
- **Linguagem de Programação**: Python 3.9.13.
- **Biblioteca para Blockchain**: `web3`.
- **Integração com IA**: Possibilidade de enviar o resultado do modelo de IA treinado na Parte 1 para armazenamento seguro na Blockchain.




