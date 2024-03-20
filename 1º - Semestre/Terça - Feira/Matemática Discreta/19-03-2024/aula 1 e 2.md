# condição de igualdade

representado por: p ≡ q ou p ↔ q

tabela 
| p | q | p ↔ q |
|---|---|-------|
| V | V | V     |
| V | F | F     |
| F | V | F     |
| F | F | V     |

## Exercicio

dado p = verdadeiro e q = falso

1. p ^ q                   (F)
2. ~(p V ~q)               (V)
3. ~p → q                  (V)
4. ~(p ↔ q)                (V)




```
() (32 - 3 * 12 = -4 ^ 12 + 15 = 27)
() (15 + 2 ≠ 17 v 18 - 9 = 9)
() (12 / 4 = 4 ↔ 25 - 13 = 12)
() (48 / 4 = 12 → 16 + 17 ≠ 33)
() (13 / 12 = 9 v1 + 1 = 3)
```
alternativa (b) V, V, F, F, F

## Construção das tabelas verdades

Uso de parenteses

A necessidade de usar parenteses devem ser colocados para evitar qualquer tipo de ambiguidade

```a ordem de precendencia```
```
(1) ~
(2) ^ e v
(3) →
(4) ↔
```

o conceito mais fraco é ~ e o mais forte é ↔

a) ~(p v ~q)

| p | q | ~q | p v ~q | ~(p v ~q) |
|---|---|----|--------|-----------|
| V | V | F  | V      | F         |
| V | F | V  | V      | F         |
| F | V | F  | F      | V         |
| F | F | V  | V      | V         |

b) ~(p → ~q)
| p | q | ~q | p → ~q | ~(p → ~q) |
|---|---|----|--------|-----------|
| V | V |
| V | F |
| F | V |
| F | F |



c) p ^ q → p v q
| p | q | p ^ q | p v q  | p ^ q → p v q |
|---|---|-------|--------|---------------|
| V | V |  V    |   V    |   V           |
| V | F |  V    |   F    |   F           |
| F | V |
| F | F |
