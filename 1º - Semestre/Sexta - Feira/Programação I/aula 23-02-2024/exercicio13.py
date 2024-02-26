#Leia uma distancia em quil ˆ ometros e apresente-a convertida em milhas. A f ˆ ormula de ´
#conversao˜ e: ´ M = K 1,61 , sendo K a distancia em quil ˆ ometros e ˆ M em milhas.

def kmToMiles(km):
    return km / 1.61

if __name__ == '__main__':
    km = float(input('digite o valor me km para ser convertido:'))
    print('valor em milhas:', milesToKm(km))