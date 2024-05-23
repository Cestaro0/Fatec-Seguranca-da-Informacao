# Estrutura condicional

```py
if (condição):
elif (condição):
else:
```

## Exercicio 
dado um numero inteiro ou real, verificar se o numero é positivo negativo ou nulo

```py
if __name__ == '__main__':
  numero = float(input('digite um numero: '))
  
  if (numero > 0):
    print('numero positivo')
  elif (numero < 0):
    print('numero negativo')
  else:
    print('numero nulo')
```

## Exercicio 2
```py
a, b, c = map(float, input('entre com 3 medidas de um triangulo').split())
a = float(a)
b = float(b)
c = float(c)

if ( a == b) and (c == b):
 print('equilatero')
elif (a != b) and (a != c) and (b != c):
 print('escaleno')
else:
 print('isósceles')
 
