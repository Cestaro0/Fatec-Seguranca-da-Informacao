# Resolva 

D)
| ~p | q | ~p |  q → p | ~p → ( q → p ) |
|----|---|----|--------|----------------|
| V  | V | F  | V      |  V             |
| V  | F | F  | V      | V              |
| F  | V | V  | F      | F              |
| F  | F | V  | V      | V              |

E)

![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/f8f0d3f8-c48b-4a9d-bd1c-8a8d58d85656)

resolução:
| p | q | p → q | p ^ q | (p → q) → (p ^ q) |
|---|---|-------|-------|-------------------|
| V | V | V     | V     |    V              |
| V | F | F     | F     | V                 |
| F | V | V     | F     | F                 |
| F | F | V     | F     | F                 |


F)

![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/20996bcb-ad4f-490b-a960-b14270091d6c)

| p | q | ~q | ~q ^ p | q ↔ ~q ^ p|
|---|---|----|--------|-----------|
| V | V | F  | F      | F         |
| V | F | V  | V      | F         |
| F | V | F  | F      | F         |
| F | F | V  | F      | V         |


## taltologia (apenas verdade) e contradição (apenas falso)

exemplo:
a) p ^ ~p é? contradição
b) p v ~p é? taltologia

| p | ~p | p ^ ~p | p v ~p |
|---|----|--------|--------|
| V | F  | F      |  V     |
| F | V  | F      |  V     |


![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/7394b439-3603-48c3-a94c-080364bde77a)

| p | q | r | q ^ r | p v (q ^ r) | p v q | p v r | (p v q) ^ (p v r) | p v (q ^ r) ↔ (p v q) ^ (p v r) |
|---|---|---|-------|-------------|-------|-------|-------------------|---------------------------------|
| V | V | V |   V   |   V         |  V    | V     |         V         |       V                         |
| V | V | F |   F   |   V         |  V    | V     |         V         |       V                         |
| V | F | V |   F   |   V         |  V    | V     |         V         |       V                         |
| V | F | F |   F   |   V         |  V    | V     |         V         |       V                         |
| F | V | V |   V   |   V         |  V    | V     |         V         |       V                         |
| F | V | F |   F   |   F         |  V    | F     |         F         |       V                         |
| F | F | V |   F   |   F         |  F    | V     |         F         |       V                         |
| F | F | F |   F   |   F         |  F    | F     |         F         |       V                         |



