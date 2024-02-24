#Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
#A formula de conversao e: F = C∗(9.0/5.0)+32.0, sendo F a temperatura em Fahrenheit
#e C a temperatura em Celsius.


def celsiusToFarenheit(graus):
    return graus * (9.0 / 5.0) + 32.0

if __name__ == '__main__':
    celsius = float(input('Digite a temperatura em celsius:'))
    print('A temperatura em farenheit e:', celsiusToFarenheit(celsius))