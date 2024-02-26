# Leia um valor de volume em litros e apresente-o convertido em metros cubicos ´ m3 . A
#formula de convers ´ ao˜ e: ´ M = L 1000 , sendo L o volume em litros e M o volume em metros
#cubicos.

if __name__ == '__main__':
    n = float(input('digite um volume em litros:'))
    print('o valor convertido para metros cubicos e:', n / 1000)