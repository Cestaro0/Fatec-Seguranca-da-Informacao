#Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A
#formula de conversao e: K = C + 273.15, sendo C a temperatura em Celsius e K a
#temperatura em Kelvin.

def celsiusToKelvin(graus):
    return graus - 273.15

if __name__ == '__main__':
    
    celsius = float(input('Digite a temperatura em celsius:'))
    print('A temperatura em kelvin e:', celsiusToKelvin(celsius))