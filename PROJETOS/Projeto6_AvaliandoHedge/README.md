# Projeto 6 - Engenharia Financeira com IA: Estruturação de Derivativos para Hedging de Riscos de Commodities

Este projeto explora o uso de técnicas de Engenharia Financeira com Inteligência Artificial para estruturar derivativos financeiros que ajudem a mitigar riscos associados à volatilidade no preço de commodities, especificamente o petróleo. As três etapas do projeto cobrem a geração de dados simulados, a modelagem estatística e a aplicação de IA para estratégias de hedge.

## Estrutura do Projeto

### Etapa 1: Geração de Dados

- **Objetivo**: Simular uma série temporal de preços de petróleo ao longo de 365 dias para servir de base para a modelagem e a análise.
- **Conteúdo**:
  - Simulação de preços com base em um modelo de movimento geométrico browniano (GBM), incorporando drift e volatilidade diários.
  - Visualização dos preços simulados ao longo do período.
- **Parâmetros**:
  - **Preço inicial**: 50 USD por barril.
  - **Volatilidade diária**: 0.1 (10%).
  - **Drift diário**: 0.0002 (0.02%).
- **Resultado**: Criação do arquivo `preco_petroleo.csv` com os dados simulados e um gráfico que mostra a variação de preços ao longo de 365 dias.

### Etapa 2: Modelagem Estatística

- **Objetivo**: Usar um modelo ARIMA para prever os preços do petróleo nos próximos 30 dias, identificando tendências e volatilidade esperada.
- **Conteúdo**:
  - Treinamento de um modelo ARIMA na série temporal de preços simulados.
  - Cálculo do drift e volatilidade com base nos retornos previstos pelo modelo.
- **Simulação de Monte Carlo**: Usando os parâmetros de drift e volatilidade previstos pelo ARIMA, são realizadas 1000 simulações para projetar os preços do petróleo nos próximos 30 dias.
- **Estratégia de Hedge**: Comparação entre o custo futuro do petróleo com e sem hedge, considerando um contrato de futuros a 45 USD por barril.
- **Resultado**: Avaliação de uma estratégia de hedge baseada em previsões estatísticas.

### Etapa 3: Inteligência Artificial

- **Objetivo**: Implementar um modelo de rede neural LSTM para prever os retornos diários do petróleo e calcular o drift e volatilidade para uma estratégia de hedge baseada em IA.
- **Conteúdo**:
  - Construção e treinamento de uma LSTM com `TensorFlow` para prever os retornos do petróleo com base em uma janela de 30 dias de retornos passados.
  - Cálculo do drift e volatilidade com base nas previsões da LSTM.
- **Simulação de Monte Carlo**: Realização de 1000 simulações para projetar os preços do petróleo nos próximos 30 dias, utilizando os parâmetros previstos pela LSTM.
- **Estratégia de Hedge**: Avaliação do custo futuro do petróleo com e sem hedge, com o mesmo contrato de futuros a 45 USD por barril.
- **Resultado**: Comparação do custo futuro com hedge baseado em IA versus sem hedge, visualizando a economia potencial com o uso da estratégia.

---

## Como Utilizar este Repositório

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/IA_Financas_HedgeCommodities.git

