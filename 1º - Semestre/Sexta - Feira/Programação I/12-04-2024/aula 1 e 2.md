# Funções

```py

def soma(a, b):
  print('Soma vale {:.2f}'.format(a + b))

def sub(a, b):
  print('Subtracao vale {:.2f}'.format(a - b))

def leitura():
  a, b = map(float, input('Digite dois numeros:').split())

  return a, b

if __name__ == '__main__':
  a, b = leitura()
  soma(a, b)
  sub(a, b)
```


Escreva uma função que recebe como parametro um numero inteiro N e calcule o fatorial
```py
import math

def fatorial(n):
  ft = 1

  for i in range (n, 1):
    ft *= x

  return ft

if __name__ == '__main__':
  n = int(input('digite um numero:'))
  print('Fatorial vale {:d}'.format(fatorial(n)))
```
