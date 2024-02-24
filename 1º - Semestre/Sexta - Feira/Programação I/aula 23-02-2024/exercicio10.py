#Leia uma velocidade em km/h (quilometros por hora) e apresente-a convertida em m/s ˆ
#(metros por segundo). A formula de conversao e: M = K/3.6, sendo K a velocidade em
#km/h e M em m/s.

if __name__ == '__main__':
    kmH = float(input('Digite o km/h para ser convertido:'))
    print('o valor convertido em m/s:', kmH / 3.6)