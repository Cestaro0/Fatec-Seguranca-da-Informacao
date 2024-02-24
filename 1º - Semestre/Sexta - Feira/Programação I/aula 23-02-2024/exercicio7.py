#Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
#A formula de conversao e: C = 5.0 ∗ (F − 32.0)/9.0, sendo C a temperatura em Celsius
#e F a temperatura em Fahrenheit.


def farenheitToCelsius(graus):
    return 5.0 * (graus - 32.0) / 9.0

if __name__ == '__main__':
    
    farenheit = float(input('Digite a temperatura em farenheit:'))
    print('A temperatura em celsius e:', farenheitToCelsius(farenheit))