# Leia um valor de comprimento em polegadas e apresente-o convertido em cent´ımetros.
#A formula de convers ´ ao˜ e:´ C = P ∗ 2, 54, sendo C o comprimento em cent´ımetros e P o
#comprimento em polegadas.


if __name__ == '__main__':
    n = float(input('digite um valor em polegadas:'))
    print('o valor de polegadas para centimettros e:', n * 2.54)