# Bases numericas

hex: B6 63 A1 17 95 C2

bin: 1011 0110 0110 0011 1010 0001 0001 0111 1001 0101 1100 0010

oct: 101 101 100 110 001 110 100 001 000 101 111 001 010 111 000 010

oct:  5   5   4   6   1   6   4   1   0   5   7   1   2   7   0   2

# Conversão de base decimal
```
10 -> 2
10 -> 8           Divisão sucessiva pela base de destino
10 -> 16
```

converta 1492 da base 10 pra base 2

```
1492 / 2 = 746, resto 0
746 / 2 = 373, resto  0
373 / 2 = 186, resto  1
186 / 2 = 93, resto   0
93 / 2 = 46, resto    1
46 / 2 = 23, resto    0
23 / 2 = 11, resto    1
11 / 2 = 5, resto     1
5 / 2 =  2, resto     1
2 / 2 =  1, resto     0
1 / 2 =  0, resto     1 
```
O resultado é visto de baixo para cima, então: 10111010100

converta 1492 da base 10 para a base 8

```
1492 / 8 = 186, resto 4
186 / 8 = 23, resto   2
23 / 8 = 2, resto     7
2 / 8 = 0, resto      2
```

O restultado é visto de baixo para cima, então: 2724

Converta 1492 da base 10 para a base 16

```
1492 / 16 = 93, resto 4
93 / 16 = 5, resto    D
5 / 16 = 0, resto     5
```

O resultado é visto de baixo pra cima, então: 5d4


Conversão de numeros decimais quando é com virgula **Multiplicação**

```
0.25 x 2 = 0.5 -> 0
0.5 x 2 = 1    -> 1
```

O resultado é lido de cima para baixo, então: 0.01

## Conversão de uma base para outra
Conversão de qualquer base para 10

![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/5451e2ee-9833-4f6d-89d7-6c9aaa1d9ac1)

converta 10101101² -> 10
```
1*2^7 + 0*2^6 + 1*2^5 + 0*2^4 + 1*2^3 + 1*2^2 + 0*2^1 + 1*2^0
128 + 0 + 32 + 0 + 8 + 4 + 0 + 1
172 + 1 = 173
```

Converta 5d4 -> 10
```
5 * 16 + D * 16 + 4 * 16
5 * 16^2 + 13 * 16^1 + 4 * 16^0
5 * 256 + 13 * 16 + 4*1
1280 + 208 + 4
1492
```
