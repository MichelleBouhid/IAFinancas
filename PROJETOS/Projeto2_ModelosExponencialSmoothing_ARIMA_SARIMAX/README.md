# IA Aplicada a Finanças: Forecast de Títulos de Renda Fixa

Este projeto faz parte de uma série de estudos para aplicação de técnicas de Machine Learning e Inteligência Artificial em Finanças, especificamente para previsão (forecast) de títulos de renda fixa ao longo do tempo. O objetivo deste projeto é explorar e comparar diferentes modelos de previsão em séries temporais financeiras.

## Estrutura do Projeto

Cada notebook representa uma etapa específica de modelagem preditiva, aumentando a complexidade e a capacidade de previsão a cada passo. Abaixo está uma descrição de cada parte.

### Parte 1: Métodos Naive e Suavização Exponencial

- **Objetivo**: Iniciar com métodos de previsão básicos, como o método Naive e técnicas de Suavização Exponencial.
- **Conteúdo**: Este notebook apresenta os fundamentos de previsão de séries temporais com métodos simples, que servem como base de comparação para modelos mais complexos.
- **Técnicas**:
  - **Método Naive**: Usado como baseline para avaliar a eficácia de modelos mais avançados.
  - **Suavização Exponencial**: Aplica suavização para capturar tendências leves em dados de séries temporais.
- **Resultado Esperado**: Obter previsões básicas que permitam estabelecer uma linha de base para futuras comparações.

### Parte 2: Modelo ARIMA

- **Objetivo**: Implementar o modelo ARIMA (AutoRegressive Integrated Moving Average) para prever séries temporais com base na autocorrelação dos dados.
- **Conteúdo**: O notebook aprofunda-se no modelo ARIMA, explicando como ajustar parâmetros para capturar padrões temporais.
- **Técnicas**:
  - Análise de autocorrelação e autocorrelação parcial (ACF e PACF).
  - Ajuste dos parâmetros do modelo ARIMA (`p`, `d`, `q`).
- **Resultado Esperado**: Obter previsões mais precisas em comparação com os métodos simples, considerando a estrutura temporal da série.

### Parte 3: Modelo SARIMAX

- **Objetivo**: Aplicar o modelo SARIMAX (Seasonal ARIMA with eXogenous factors), que adiciona sazonalidade e permite variáveis exógenas na previsão.
- **Conteúdo**: Explora a modelagem sazonal e o uso de variáveis exógenas, que podem melhorar a precisão da previsão em séries temporais financeiras.
- **Técnicas**:
  - Ajuste de parâmetros sazonais (`P`, `D`, `Q`, `s`) para capturar padrões sazonais.
  - Inclusão de variáveis exógenas, se aplicável, para enriquecer a previsão.
- **Resultado Esperado**: Um modelo mais robusto que lida bem com sazonalidade e fatores externos, proporcionando uma previsão mais precisa e realista para a série.

---

## Como Utilizar este Repositório

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/IA_Financas_Projeto2.git

