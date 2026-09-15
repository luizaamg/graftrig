# Gerador de Gráficos Trigonométricos

## Sobre o Projeto
Este projeto consiste em um script interativo desenvolvido em Python para a geração e visualização de gráficos de funções trigonométricas. A ferramenta permite que qualquer pessoa manipule parâmetros matemáticos em tempo real pelo terminal, facilitando o estudo visual de como essas alterações afetam a forma geométrica da onda no plano cartesiano.

## Funcionalidades
*   **Geração de Ondas:** Suporte para calcular e plotar as equações trigonométricas `f(x) = a * sen(bx + c) + d` e `g(x) = a * cos(bx + c) + d`.
*   **Parâmetros Customizáveis:** O usuário é guiado para definir variáveis exatas como amplitude (a), controle de frequência (b), deslocamento horizontal (c) e deslocamento vertical (d).
*   **Visualização Intuitiva:** A interface gráfica gerada inclui os eixos X e Y demarcados, grade de fundo (grid), legenda com a equação formatada e distinção de cores automáticas (azul para seno, vermelho para cosseno).
*   **Prevenção de Erros:** O algoritmo inclui blocos de tentativa (`try/except`) para alertar o usuário e evitar a quebra do programa caso sejam digitados caracteres inválidos no lugar de números.

## Pré-requisitos e Instalação
Para rodar este código localmente, você precisará preparar o seu ambiente:
*   Certifique-se de ter o Python instalado no seu computador.
*   Você precisará instalar as bibliotecas `numpy` e `matplotlib` caso ainda não as tenha.
*   Para realizar essa instalação, basta abrir o terminal ou prompt de comando do seu sistema e digitar o comando: `pip install numpy matplotlib`

## Como Executar
*   Copie o código e salve-o em um arquivo, nomeando-o, por exemplo, como `grafico_trigonometrico.py`.
*   Abra o seu terminal na mesma pasta onde o arquivo foi salvo.
*   Execute o script digitando `python grafico_trigonometrico.py`.
*   Siga as perguntas que aparecerão no console para inserir os valores numéricos e escolher a função desejada ('sen' ou 'cos').
*   Imediatamente após as respostas, uma janela interativa se abrirá exibindo a figura da função plotada.
