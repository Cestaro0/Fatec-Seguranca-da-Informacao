#Fac¸a um programa que leia o valor da hora de trabalho (em reais) e numero de horas ´
#trabalhadas no mes. Imprima o valor a ser pago ao funcion ˆ ario, adicionando 10% sobre ´
#o valor calculado.

if __name__ == '__main__':
    hrs = float(input('digite o valor das horas de um trabalhador:'))
    hrsMes = float(input('digite as horas de trabalho:'))
    
    print('o salario e:', hrs * hrsMes + (hrs * hrsMes) * 0.1)
    