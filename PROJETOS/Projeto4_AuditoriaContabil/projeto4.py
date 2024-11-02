# Projeto 4 - Auditoria Contábil com Inteligência Artificial

# pip install optuna  #pacote python para otimização de hiperparâmetros

# Imports
import optuna #otimização dos hiperparametros
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN #pacote cluster e dentro o pacote DBSCAN
from sklearn.preprocessing import StandardScaler #pacote preprocessing e dentro a função StandardScaler
# Que permite criar um padronizador dos dados, importante no trabalho com tecnicas de clusterização.
# Clusterização - devemos deixar os dados na mesma escala!
from sklearn.metrics import silhouette_score # medida de avaliação de algoritmo de clusterização
# Como não temos valores de saídas nos dados, não temos como usar metricas de aprendizado supervisionado como acurácia, precisão 
import warnings
warnings.filterwarnings('ignore')

# Carrega os dados
df = pd.read_csv('transacoes_contabeis.csv')

# Converte a data da transação para uma representação numérica - usando como categoria.
# Nesse projeto não estamos trabalhando com séries temporais, não precisamos colocar data como indice
# Nesse projeto queremos agrupar os dados por similaridade, não precisamos de ordem cronologica como série temporais
# Como a data tem traço - computador interpreta como variável categorica, texto que não pode ser usado nesse caso.  
# Como temos mtas datas repetidas se comportando como categoria.
# Vamos usar a data como categoria, converte em datetime e depois converte pra inteiro no formato do Numpy
df['Data_Transacao'] = pd.to_datetime(df['Data_Transacao']).astype(np.int64)

# Seleciona as colunas que vamos usar para identificar possíveis atividades de smurfing
atributos = ['ID_Conta', 'Data_Transacao', 'Valor']
X = df[atributos]

# Normalizar os recursos para que eles tenham uma média de 0 e um desvio padrão de 1
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Definindo a função de otimização que será utilizada pelo optuna
def optimize(trial):

    # Define um valor para 'eps' no intervalo de 0.1 a 1.0 usando o objeto `trial`
    eps = trial.suggest_float('eps', 0.1, 1.0)

    # Define um valor inteiro para 'min_samples' no intervalo de 2 a 10 usando o objeto `trial`
    min_samples = trial.suggest_int('min_samples', 2, 10)

    # Instancia o algoritmo DBSCAN com os parâmetros sugeridos anteriormente
    dbscan = DBSCAN(eps = eps, min_samples = min_samples)

    # Aplica o algoritmo DBSCAN no conjunto de dados X e retorna as etiquetas para cada ponto de dado
    labels = dbscan.fit_predict(X)
    
    # Usamos o coeficiente silhouette para avaliar a qualidade dos clusters. 
    # O coeficiente silhouette varia de -1 a 1. 
    # Valores Próximos de 1: Indicam que os pontos são muito semelhantes aos outros pontos do cluster e diferentes dos pontos de outros clusters.
    # Valores Próximos de 0: Indicam que os pontos estão próximos da fronteira de decisão entre dois clusters.
    # Valores Próximos de -1: Indicam que os pontos foram atribuídos ao cluster errado.
    # Como o coeficiente silhouette é indefinido para um único cluster, verificamos se temos mais de um cluster antes de calcular.
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    if n_clusters > 1:
        score = silhouette_score(X, labels)
    else:
        score = -1
    return score

# Otimizando os hiperparâmetros
study = optuna.create_study(direction = 'maximize')
study.optimize(optimize, n_trials = 100)

# Obter os melhores hiperparâmetros
best_params = study.best_params

# Cria o DBSCAN com os melhores hiperparâmetros
dbscan = DBSCAN(eps = best_params['eps'], min_samples = best_params['min_samples'])

# Treina o DBSCAN com os melhores hiperparâmetros
df['Cluster'] = dbscan.fit_predict(X)

# Encontraremos agora os clusters que têm um número de transações acima de um determinado limiar.
# Nesse caso, estamos usando um limiar de 5, mas você pode ajustá-lo conforme necessário.
limiar = 5
clusters_suspeitos = df['Cluster'].value_counts()[df['Cluster'].value_counts() > limiar].index

# Extraindo as transações nos clusters suspeitos
transacoes_suspeitas = df[df['Cluster'].isin(clusters_suspeitos)]

# Filtrando o dataframe com base no valor da coluna 'Cluster'
filtrado = transacoes_suspeitas[transacoes_suspeitas['Cluster'] == -1]

# Na implementação DBSCAN do scikit-learn, o rótulo de cluster -1 significa que a amostra foi considerada como ruído.

# O DBSCAN, que significa "Density-Based Spatial Clustering of Applications with Noise", é um algoritmo de agrupamento que cria clusters de 
# regiões de alta densidade no espaço de recursos e identifica amostras individuais que estão em áreas de baixa densidade como ruído.

# Divide os dados em grupos, com base em distancia matemática, se algum dado não couber em nenhum grupo, identifica como anomalia.

# Usa o Optuna, um pacote Python para otimizar hiperparametros e o DBSCAN que é um algoritmo de aprendizado de máquina não supervisionado

# Portanto, em nosso contexto, se uma transação é rotulada com o cluster -1, isso significa que ela não foi incluída em nenhum dos 
# clusters densos de transações formados pelo DBSCAN e foi considerada "ruído". Isso poderia potencialmente indicar uma transação incomum ou anômala, 
# dependendo do contexto específico e dos parâmetros do algoritmo.

# Selecionando as colunas desejadas
resultado = filtrado[['ID_Conta', 'Valor', 'Cluster']]

# Salva o resultado em disco
resultado.to_csv('transacoes_suspeitas.csv', index = False)

# Fim

