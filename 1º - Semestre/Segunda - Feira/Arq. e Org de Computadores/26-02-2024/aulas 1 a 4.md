# Numeros binarios

A aritmetica usada por computadores é um pouco diferente daquela utilizada pelas pessoas.
diferença: É que os computadores realizam numeros binarios para comunicação

## Precisão finita

IPV4 - 2³²: 192.168.10.25

IPV6 - 2¹²⁸

Numeros de precisao finita acabam invalidadndo essas quatro operações basicas, como mostrado a seguir , se usarmos números decimais de três digitos como exemplo:
```
600 + 600 = 1200 (muito grande)
003 - 005 = -002 (negativo)
050 * 050 = 2500 (muito grande)
007 / 002 = 3.50 (não é inteiro)
```

A algebra de numeros de precisao finita é diferente da algebra normal.

como por exwemplo, considere a lei associativa:

```
a + (b - c) = (a + b) - c
```

outra é a lei distributiva 
```
a * (b - c) = a * b - a * c
```

# Sistemas de numeros raiz, ou numeros base

Um numero decimal ordinario com o qual todos estamos familiarizados consiste e em uma sequencia de digitos decimais e, possivelmente, um ponto decimal (virgula aritmetica)

Escolhemos 10 como a base da exponenciação, denominada a raiz da base, porque estamos usando numeros decimais, ou de base 10

exemplo:
125.35

```
1 * 100 + 2 * 10 + 5 * 1 + 3 * 0.1 + 5 * 0.01
OU 
1 * 10² + 2 * 10¹ + 5 * 10º + 3 * 10-¹ + 5 * 10-²
```

as bases para o computadores mais importantes são: 2, 8, 10, 16
```
bin: 0 a 1
octal: 0 a 7
dec: 0 a 9
hex: 0 a F
```
![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/b94726f0-81a1-4a19-8dcb-5781fc4ec95e)


# Conversão de uma base para outra
```
oct <-> bin
hex <-> bin     TABELA
oct <-> hex
```

bin to oct
```
000 - 0
001 - 1
010 - 2
011 - 3
100 - 4
101 - 5
110 - 6
111 - 7
```

bin to hex

```
0000 - 0
0001 - 1
0010 - 2
0011 - 3
0100 - 4
0101 - 5
0110 - 6
0111 - 7
1000 - 8
1001 - 9
1010 - A
1011 - B
1100 - C
1101 - D
1110 - E
1111 - F
```

exemplo de conversão bin to hex
```
hex  1    9   8    8       B    6
bin 0001 1001 0100 1000 , 1011 0110
```


exemplo de conversão bin to oct
```
bin 0 001 100 101 001 000 , 101 101 100
oct    1   7   5   1   0     5   5   4
```

Converta FEDID0 em octal e binario

```
1111 1110 1101 0001 1101 0000

111 111 101 101 000 111 010 000
 7   7   5   5   0   7   2   0
```

converta FA7EC em octal e binario
```
1111 1010 0111 1110 1100

011 111 010 011 111 101 100
3    7   2   3   7   5   4
```
converta FACA em octal e binario
```
1111 1010 1100 1010

001 111 101 011 001 010
1    7   5   3   1   2
```
