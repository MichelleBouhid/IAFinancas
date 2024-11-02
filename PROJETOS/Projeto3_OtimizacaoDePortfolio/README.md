# IA Aplicada a Finanças: Otimização de Portfólio de Ativos Financeiros

Este projeto explora técnicas de otimização de portfólio aplicadas a ativos financeiros, com o objetivo de maximizar o retorno ajustado ao risco. Inspirado na teoria moderna de portfólio de Harry Markowitz, foram implementadas três estratégias de otimização usando o pacote PyPortfolioOpt.

## Estrutura do Projeto

Cada estratégia representa uma abordagem diferente de otimização, explorando parâmetros e métodos variados para atender a diferentes perfis de risco e objetivos de retorno. Abaixo está um resumo das estratégias.

### Estratégia 1: Otimização Baseada nos Valores Passados

- **Objetivo**: Construir um portfólio com base em dados históricos de retorno, buscando maximizar o índice de Sharpe.
- **Conteúdo**: Utiliza o histórico de retornos e a variância dos ativos para definir uma alocação otimizada.
- **Técnicas**:
  - Cálculo da Fronteira Eficiente.
  - Maximização do índice de Sharpe.
- **Resultado Esperado**: Um portfólio eficiente que considera o desempenho passado dos ativos.

### Estratégia 2: Otimização com Previsão de Valores Futuros por IA

- **Objetivo**: Incorporar previsões de retornos futuros baseadas em modelos de IA para construir o portfólio.
- **Conteúdo**: Usa previsões de IA para ajustar a alocação de ativos, tentando melhorar o retorno esperado.
- **Técnicas**:
  - Modelos de previsão (insira o modelo utilizado, como ARIMA, SARIMAX, etc., caso aplique).
  - Cálculo de alocação com base em retornos previstos.
- **Resultado Esperado**: Uma alocação que leva em conta possíveis cenários futuros, ajustando-se às expectativas de mercado.

### Estratégia 3: Otimização com Minimização de CVaR

- **Objetivo**: Otimizar o portfólio com base nas previsões de IA, mas também minimizando o Conditional Value at Risk (CVaR).
- **Conteúdo**: Integra previsões e uma medida de risco extremo (CVaR), para criar um portfólio mais robusto.
- **Técnicas**:
  - Otimização da Fronteira Eficiente.
  - Minimização do CVaR.
- **Resultado Esperado**: Um portfólio que busca mitigar perdas extremas, adequado para investidores mais avessos ao risco.

---

## Uso de Pacotes e Ajuste de Parâmetros

Neste projeto, foi utilizado o pacote **PyPortfolioOpt** para otimização do portfólio. Embora o pacote ofereça funcionalidades prontas, os parâmetros de entrada precisam ser cuidadosamente observados e ajustados com base no perfil de risco e retorno desejado.

> **Nota**: Este projeto replica uma abordagem ensinada em aula, mas foi adaptado para diferentes ativos. O ajuste dos parâmetros e a escolha dos ativos foram feitos de acordo com o contexto de dados históricos disponíveis. É recomendável que o usuário teste diferentes parâmetros e ativos para entender o comportamento do portfólio sob diversas condições.

## Como Utilizar este Repositório

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/IA_Financas_Projeto3.git

