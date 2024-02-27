#Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume
#de um cilindro circular ´e calculado por meio da seguinte f ´ ormula: V =   raio2  altura,
#onde  = 3:141592.

import math

if __name__ == '__main__':
    alt = float(input('digite a altura do cilindro:'))
    r = float(input('digite o raio da base do cilindro:'))

    print('o volume do cilindro e: ', math.pi * r **2 * alt)