# IA Aplicada a Finanças: Auditoria Contábil com Inteligência Artificial

Este projeto aplica técnicas de aprendizado de máquina não supervisionado para identificar transações contábeis incomuns ou potencialmente fraudulentas. A abordagem se baseia no algoritmo DBSCAN para detecção de anomalias em transações financeiras, auxiliado pelo Optuna para otimização de hiperparâmetros.

## Estrutura do Projeto

Este projeto de auditoria contábil utiliza clustering para agrupar transações similares e identificar aquelas que são consideradas "ruído", ou seja, transações que não se encaixam em nenhum cluster denso, podendo indicar anomalias. Abaixo estão os detalhes dos principais componentes.

### Objetivo: Identificar Anomalias em Transações Contábeis

- **Contexto**: No contexto de auditoria contábil, anomalias ou transações incomuns podem indicar atividades suspeitas, como fraudes. Este projeto visa identificar tais transações agrupando dados contábeis por similaridade.
- **Técnicas Utilizadas**:
  - **DBSCAN**: Algoritmo de clusterização baseado em densidade, ideal para detectar clusters de diferentes formas e identificar pontos de dados que não pertencem a nenhum cluster (marcados como ruído).
  - **Optuna**: Pacote para otimização de hiperparâmetros, usado aqui para encontrar os melhores valores de `eps` e `min_samples` do DBSCAN.

### Conteúdo do Projeto

- **Pré-processamento**: 
  - Conversão de datas para representação numérica, uma vez que o objetivo é agrupar transações similares, não sendo necessário manter uma ordem cronológica.
  - Padronização dos dados usando `StandardScaler` para garantir que todas as variáveis estejam na mesma escala, uma prática essencial em algoritmos de clusterização.
  
- **DBSCAN**: 
  - O algoritmo DBSCAN é utilizado para criar clusters de alta densidade. Ele trabalha com dois parâmetros principais: `eps` (distância máxima entre dois pontos para que sejam considerados vizinhos) e `min_samples` (número mínimo de pontos para formar um cluster).
  - Após agrupar as transações, as amostras que não se encaixam em clusters densos recebem o rótulo `-1`, indicando que foram identificadas como ruído.

- **Optuna para Otimização de Hiperparâmetros**: 
  - Optuna é utilizado para otimizar os hiperparâmetros do DBSCAN, buscando maximizar o coeficiente de silhueta, uma métrica que avalia a qualidade dos clusters formados.
  - Os melhores valores de `eps` e `min_samples` são selecionados com base nessa métrica, melhorando a performance do modelo.

### Resultado Esperado

- **Identificação de Transações Anômalas**: Transações que são rotuladas com o cluster `-1` pelo DBSCAN são tratadas como "ruído" e podem representar transações incomuns ou suspeitas.
- **Exportação de Resultados**: As transações anômalas são exportadas para um arquivo `transacoes_suspeitas.csv` para análise posterior.

---

## Como Utilizar este Repositório

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/IA_Financas_Projeto4.git

