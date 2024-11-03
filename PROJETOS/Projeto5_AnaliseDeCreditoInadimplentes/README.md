# IA Aplicada a Finanças: Previsão de Inadimplência com Base em Análise de Crédito

Este projeto utiliza técnicas de Inteligência Artificial para prever a inadimplência de clientes com base no histórico de crédito. O modelo foi desenvolvido para auxiliar instituições financeiras a identificar, de forma antecipada, potenciais inadimplentes, permitindo decisões mais informadas no processo de concessão de crédito.

## Estrutura do Projeto

O projeto é dividido em duas partes principais: Treinamento e Teste do modelo e Deploy do modelo. Utilizando redes neurais com PyTorch, a solução oferece uma abordagem robusta e interpretável para a previsão de inadimplência.

### Parte 1: Treinamento e Teste do Modelo

- **Objetivo**: Treinar um modelo de rede neural para classificação binária (inadimplente ou não) com base no histórico de crédito e em características financeiras dos clientes.
- **Conteúdo**: 
  - Pré-processamento dos dados, incluindo padronização com `StandardScaler` para garantir que todas as variáveis estejam na mesma escala.
  - Construção de uma rede neural com PyTorch, composta por quatro camadas totalmente conectadas e ativação sigmoide na última camada para previsão de probabilidade.
  - Função de perda de **Binary Cross Entropy Loss (BCE)**, adequada para problemas de classificação binária.
- **Técnicas**:
  - Divisão dos dados em conjuntos de treino e teste.
  - Otimização dos parâmetros da rede neural utilizando o otimizador **Adam**.
  - Avaliação da perda durante o treinamento para monitorar o desempenho.
- **Resultado Esperado**: Obter um modelo de rede neural treinado capaz de prever a probabilidade de inadimplência dos clientes, com os pesos e parâmetros salvos para deploy.

### Parte 2: Deploy do Modelo

- **Objetivo**: Implementar o modelo treinado para realizar previsões sobre novos clientes.
- **Conteúdo**:
  - Carregamento do modelo treinado e do `StandardScaler` para padronizar novos dados de clientes.
  - Realização de previsões com base em um limiar de 0.5 para classificar clientes como inadimplentes ou não.
  - Armazenamento dos resultados das previsões em um arquivo CSV, permitindo análise posterior.
- **Técnicas**:
  - Conversão dos dados de entrada para tensores com PyTorch.
  - Classificação dos clientes como "provavelmente inadimplente" ou "provavelmente não inadimplente" com base nas probabilidades calculadas.
- **Resultado Esperado**: Uma solução de deploy que permita prever a inadimplência de novos clientes e exportar os resultados em formato CSV.

---

## Como Utilizar este Repositório

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/IA_Financas_ProjetoInadimplencia.git

