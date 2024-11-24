### O que é **LSTM (Long Short-Term Memory)?**

O **LSTM** é um tipo de **Rede Neural Recorrente (RNN)** projetado especificamente para lidar com **dependências de longo prazo** em dados sequenciais, como séries temporais, texto ou outros tipos de dados em que a ordem importa. Foi introduzido para superar as limitações das RNNs clássicas, que têm dificuldades em aprender padrões em sequências longas devido ao problema do **gradiente desaparecido**.

---

### Por que usar LSTM?
As RNNs clássicas funcionam bem com dependências curtas em dados sequenciais, mas quando há relações de longo prazo (como um padrão que depende de algo ocorrido muito tempo antes), elas falham. O LSTM resolve isso com uma arquitetura que utiliza **células de memória** e **portas controladoras**, permitindo que informações relevantes sejam armazenadas ou descartadas ao longo do tempo.

---

### Como o LSTM Funciona?
O LSTM introduz um mecanismo interno chamado **célula de memória** que regula o fluxo de informações ao longo da sequência. Ele usa **três "portas" principais** para controlar como as informações são processadas:

#### **1. Porta de Esquecimento (Forget Gate)**    OBS: COLOCAR AS IMAGENS ou resolver o LATEX 
Decide **o que descartar** das informações antigas. É útil para remover informações irrelevantes.

\[
f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)
\]

- \( f_t \): vetor que indica o que esquecer.
- \( \sigma \): função sigmoide que retorna valores entre 0 (esquecer) e 1 (manter).
- \( h_{t-1} \): estado oculto anterior.
- \( x_t \): entrada atual.

---

#### **2. Porta de Entrada (Input Gate)**
Decide **o que adicionar** à célula de memória. Atualiza a memória com novas informações relevantes.

\[
i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i)
\]
\[
\tilde{C}_t = \text{tanh}(W_c \cdot [h_{t-1}, x_t] + b_c)
\]
\[
C_t = f_t \cdot C_{t-1} + i_t \cdot \tilde{C}_t
\]

- \( i_t \): vetor que indica o quanto adicionar das novas informações.
- \( \tilde{C}_t \): novos candidatos à célula de memória.
- \( C_t \): novo estado da célula de memória.

---

#### **3. Porta de Saída (Output Gate)** - ver sobre como colocar LATEX aqui
Decide **o que produzir** como saída para o próximo passo. É responsável por calcular o estado oculto \( h_t \).

\[
o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o)
\]
\[
h_t = o_t \cdot \text{tanh}(C_t)
\]

- \( o_t \): vetor que controla o que será exposto da memória.
- \( h_t \): estado oculto, que será passado como entrada para o próximo instante.

---

### Resumo do Funcionamento
1. O **estado de memória \( C_t \)** armazena informações importantes ao longo do tempo.
2. As **portas controladoras** regulam o fluxo de informações:
   - Porta de Esquecimento decide o que descartar.
   - Porta de Entrada decide o que atualizar na célula de memória.
   - Porta de Saída decide o que transmitir como saída.
3. A **função sigmoide (\( \sigma \))** controla as proporções (entre 0 e 1) para manter ou descartar informações.

---

### Exemplo Simplificado
Imagine que você está usando o LSTM para prever o preço do petróleo com base nos últimos 30 dias:
1. **Porta de Esquecimento**:
   - Remove informações irrelevantes, como valores de 2 meses atrás, que não são mais úteis.
2. **Porta de Entrada**:
   - Armazena informações dos últimos 30 dias, como tendência ou volatilidade recente.
3. **Porta de Saída**:
   - Usa a célula de memória para prever o preço do próximo dia.

---

### Vantagens do LSTM
1. **Captura de Longas Dependências**:
   - Excelente para padrões de longo prazo, como sazonalidades ou ciclos.
2. **Eficácia em Dados Sequenciais**:
   - Ideal para prever séries temporais, processar texto, e dados que mudam com o tempo.
3. **Supera RNNs Simples**:
   - Resolve problemas como **gradiente desaparecido** ou **explodido**, comuns em RNNs clássicas.

---

### Aplicações do LSTM
- **Séries Temporais**:
  - Previsão de preços financeiros como no exemplo
  - Previsão de demanda.
- **Processamento de Linguagem Natural**:
  - Tradução de texto, análise de sentimento.
- **Reconhecimento de Padrões**:
  - Reconhecimento de voz, análise de sinais biológicos.

---



