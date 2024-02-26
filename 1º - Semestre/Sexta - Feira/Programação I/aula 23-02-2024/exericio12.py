#Leia uma distancia em milhas e apresente-a convertida em quilometros. A formula de 
#conversao e: K = 1, 61 ∗ M, sendo K a distancia em quilometros e M em milhas.

def milesToKm(Miles):
    return 1.61 * Miles

if __name__ == '__main__':
    Miles = float(input('digite o valor me milhas para ser convertido:'))
    print('valor em KM:', milesToKm(Miles))