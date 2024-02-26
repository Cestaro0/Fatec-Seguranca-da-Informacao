# Leia um numero inteiro e imprima a soma do sucessor de seu triplo com o antecessor de ´ seu dobro.

if __name__ == '__main__':
    n = int(input('digite o valor:'))
    print(' a soma do sucessor de seu triplo com o antecessor de seu dobro. é:', (n * 3 + 1) + (n * 2 - 1))
