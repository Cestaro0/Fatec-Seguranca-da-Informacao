a) (p ^ ~q) v r

| p | q | r | ~q | p ^ ~p | (p ^ ~q) v r |
|---|---|---|----|--------|--------------|
| V | V | V | F  | V      | V            |
| V | F | F | V  | V      | F            |
| F | V | V | F  | F      | F            |
| F | F | F | V  | V      | F            |


| p | q | r | ~q | p ^ ~p | (p ^ ~q) v r |
|---|---|---|----|--------|--------------|
| V | V | V | F  |    F   |     V        |
| V | V | F | F  |    F   |      F       |
| V | F | V | V  |    V   |     V        |
| V | F | F | V  |    V   |     V        |
| F | V | V | F  |    V   |   V          |
| F | V | F | F  |    V   | V            |
| F | F | V | V  |    F   | V            |
| F | F | F | V  |    F   |V              |

|  p  |  q  |  r  | ~q | p ^ ~q | (p ^ ~q) v r |
|-----|-----|-----|----|--------|-------------|
|  V  |  V  |  V  |  F |   F    |      V      |
|  V  |  V  |  F  |  F |   F    |      F      |
|  V  |  F  |  V  |  V |   V    |      V      |
|  V  |  F  |  F  |  V |   V    |      V      |
|  F  |  V  |  V  |  F |   F    |      V      |
|  F  |  V  |  F  |  F |   F    |      F      |
|  F  |  F  |  V  |  V |   F    |      V      |
|  F  |  F  |  F  |  V |   F    |      V      |
