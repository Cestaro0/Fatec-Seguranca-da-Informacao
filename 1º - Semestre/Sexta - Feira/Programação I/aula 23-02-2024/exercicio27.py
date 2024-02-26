# Leia um valor de area em hectares e apresente-o convertido em metros quadrados ´ m2.
#A formula de convers ´ ao˜ e: ´ M = H ∗ 10000, sendo M a area em metros quadrados e ´ H
#a area em hectares.

if __name__ == '__main__':
    n = float(input('digite uma area hectares:'))
    print('o valor convertido para m² e:', n * 10000)