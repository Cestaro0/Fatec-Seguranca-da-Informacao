#Leia um valor de comprimento em cent´ımetros e apresente-o convertido em polegadas.
#A formula de convers ´ ao˜ e: ´ P = C 2,54 , sendo C o comprimento em cent´ımetros e P o
# comprimento em polegadas.

if __name__ == '__main__':
    n = float(input('digite um valor em centimetros:'))
    print('o valor de centimetros para polegadas e:', n / 2.54)