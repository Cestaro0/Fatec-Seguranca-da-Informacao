#Uma empresa contrata um encanador a R$ 30,00 por dia. Fac¸a um programa que solicite
#o n´umero de dias trabalhados pelo encanador e imprima a quantia l´ıquida que dever ´a ser
#paga, sabendo-se que s˜ao descontados 8% para imposto de renda.

if __name__ == '__main__':
    n = float(input('digite a quantia de dias trabalhados:'))
    valorTotal = n * 30.00
    print('o encanador recebeu com o desconto de 8 porcendto o valor de:', valorTotal - (valorTotal * 0.08))