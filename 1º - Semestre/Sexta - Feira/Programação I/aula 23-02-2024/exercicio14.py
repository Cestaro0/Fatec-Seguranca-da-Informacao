#Leia um angulo em graus e apresente-o convertido em radianos. A formula de conversao
#e: R = G ∗ π/180, sendo G o angulo em graus e ˆ R em radianos e π = 3.14.

import math

def anguloToRadiano(G):
    return G * math.pi / 180

if __name__ == '__main__':
    n = float(input('Digite um angulo em graus:'))
    print('a conversao do angulo em radiano e:', anguloToRadiano(n))