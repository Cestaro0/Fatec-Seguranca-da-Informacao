#. Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A
#formula de conversao e: C = K − 273.15, sendo C a temperatura em Celsius e K a
#temperatura em Kelvin.

def kelvinToCelsius(graus):
    return graus - 273.15

if __name__ == '__main__':
    
    kelvin = float(input('Digite a temperatura em kelvin:'))
    print('A temperatura em celsius e:', kelvinToCelsius(kelvin))