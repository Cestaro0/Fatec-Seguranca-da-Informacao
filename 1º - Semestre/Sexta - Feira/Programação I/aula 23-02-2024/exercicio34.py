#. Leia o valor do raio de um c´ırculo e calcule e imprima a area do c ´ ´ırculo correspondente.
#A area do c ´ ´ırculo e´ π ∗ raio2, considere π = 3.141592.


import math

if __name__ == '__main__':
    n = int(input('digite o valor do raio de um circulo:'))
    print('a sua area e', math.pi * n ** 2)