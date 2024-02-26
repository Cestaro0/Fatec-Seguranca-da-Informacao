# Sejam a e b os catetos de um triangulo, onde a hipotenusa ˆ e obtida pela equac¸ ´ ao: ˜
#hipotenusa =√a2 + b2. Fac¸a um programa que receba os valores de a e b e calcule
#o valor da hipotenusa atraves da equac¸ ´ ao. Imprima o resultado dessa operac¸ ˜ ao


if __name__ == '__main__':
    n1 = int(input('digite o valor do cateto 1:'))
    n2 = int(input('digite o valor do cateto 2:'))
    print('a sua area e', pow(n1 ** 2 + n2 ** 2, 0.5))