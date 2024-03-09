![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/ecf08a97-ee90-47e8-9d7b-fcd302ffe9b7)# Lógica matemática

basica para qualquer curso de computação

## Proposição
É uma sentença que ou é verdadeira ou falsa.

ex: O mercego e mamifero

a) verdadeiro

![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/3fa11342-f8d3-48b5-86ef-9aa7cceb2677)

## Conectivos
As proposições apresentadas até agora são proposições atomicas (ou atomos) que ainda não possuem conectivos, ou seja não podem ser decompostas.
Entretanto é possivel construir com operadores lógicos

EX:

![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/0baab59e-2cf6-45c0-8dad-64e212f01a69)

conectivos: **e, ou, não, se, então, se e somente se**.

## Conectivo de negação ~

p -> sempre vai ser a nossa proposição
q -> proxima proposição
r -> proxima prosposição

![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/dd884807-3292-4eff-93ca-05fc3086b841)

negação das frases:

1. Brasil não é um pais
2. linux não é um software livre
3. não é fato que 3 + 4 > 5

![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/f626919a-6598-420a-b79d-d86523e0fd9d)

Maneiras de negar uma proposição
~p

dada uma proposição p, a semantica da negação da tabela é ilustrada como:

| p |~p|
|---|---|
| V | F|
| F | V|

## Conjunção  ^ 

![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/3cdb7225-8742-4e54-8539-45f7ce715063)

dada uma proposição p e q, a semantica da conjunção entre elas é ilustrada na tabela-verdade como:

| p | q | p ^ q|
|---|---|------|
| V | V |   V  |
| V | F |   F  |
| F | V |   F  |
| F | F |   F  |

o calculo basico para saber quantas linhas terá uma tabela de verdade é baseada em X^y exemplo, uma proposição p = p¹. Duas proposições p e q = pq². Tres proposições p, q e r = pqr³...

### Exercicio

![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/ad3d866c-41d3-4fc9-8d3f-a27608e9b172)

| p | q | r | p ^ q | p ^ r | q ^ p | p ^ q ^ r|
|---|---|---|-------|-------|-------|----------|
| F | V | ? |   F   |   F   |   F   |     F    | 


## Disjunção V

![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/b90b32b4-d36c-429e-9905-6e710bb7ed8a)

dada duas proposições p e q, a semantica da disjunção de p V q é dada pela tabela-verdade como:

| p | q | p V q |
|---|---|-------|
| V | V |   V   |
| V | F |   V   |
| F | V |   V   |
| F | F |   F   |

### Exercicio

![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/2b1524d6-d815-4fac-83ed-6e73953a1aa0)

| p | q | r | p V q | p V r | q V p | p V q V r |
|---|---|---|-------|-------|-------|-----------|
| F | V | ? |   V   |   ?   |   V   |     V     | 
