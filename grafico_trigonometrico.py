import numpy as np
import matplotlib.pyplot as plt

def plotar_funcao_trigonometrica():
    print("-" * 50)
    print("Gerador de Gráficos Trigonométricos")
    print("Formato: f(x) = A.sen(bx + c) + d  ou  g(x) = A.cos(bx + c) + d")
    print("-" * 50)
    
    try:
        A = float(input("Digite o valor da amplitude (A): "))
        b = float(input("Digite o valor do controle da frequência (b): "))
        c = float(input("Digite o valor do deslocamento horizontal (c): "))
        d = float(input("Digite o valor do deslocamento vertical (d): "))
        
        funcao = input("Escolha a função trigonométrica ('sen' para seno, 'cos' para cosseno): ").strip().lower()
        
        if funcao not in ['sen', 'cos']:
            print("Erro: Função inválida! Por favor, escolha 'sen' ou 'cos'.")
            return
        # criando um intervalo para o eixo X de -2π a 2π com 1000 pontos
        x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        
        # calculo do eixo Y dependendo da função escolhida
        if funcao == 'sen':
            y = A * np.sin(b * x + c) + d
            equacao_str = f"f(x) = {A} . sen({b}x + {c}) + {d}"
            cor = 'blue'
        else:
            y = A * np.cos(b * x + c) + d
            equacao_str = f"g(x) = {A} . cos({b}x + {c}) + {d}"
            cor = 'red'

        plt.figure(figsize=(10, 6)) 
        plt.plot(x, y, label=equacao_str, color=cor, linewidth=2)

        plt.title(f"Gráfico da Função Trigonométrica\n{equacao_str}", fontsize=14, fontweight='bold')
        plt.xlabel("Eixo X (Radianos)", fontsize=12)
        plt.ylabel("Eixo Y (Amplitude)", fontsize=12)

        plt.axhline(0, color='black', linewidth=1.5) # eixo x horizontal
        plt.axvline(0, color='black', linewidth=1.5) # eixo y vertical
        
        plt.grid(True, linestyle='--', alpha=0.7)
        
        plt.legend(loc="upper right", fontsize=12)
        
        plt.xlim(-2 * np.pi, 2 * np.pi)
        
        plt.show()
        
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos para os valores de A, b, c e d.")

if __name__ == "__main__":
    plotar_funcao_trigonometrica()