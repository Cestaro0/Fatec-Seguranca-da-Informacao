# Unidade virtual

```py
Memoria ram → Volátil
  ↑ ↓
Memoria auxiliar → Fixa
```

Criação da unidade 
 - prompet de comando
 - fechar sub diretórios

### subst

Cria uma nova unicade virtual

```py
subst [DRIVE] [DRIVE:PATH]
```
exemplo:

![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/e12b703a-72f8-480a-979d-95b9be0b5746)

![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/270cd7e0-904b-41c0-a294-52b5b231dd09)

### dir
```py
dir [CAMINHO] [ARQUIVO] [OPÇÕES]
```

#### dir /p

Faz a ```pausa``` da listagem

```py
dir C:\windows /p
```

![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/4956739e-abdf-4579-8eaa-334848b77c63)

#### dir /w

faz a divisão de arquivos em ```colunas```, pastas estão em "[]"

```py
dir C:\windows /w
```

![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/3eeb2f19-3942-45dc-8b0d-33fbd7e083a9)

#### dir /s

procura o arquivo em todas as pastas
```py
dir arquivo.txt /s 
```
![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/8fc48180-5b5a-464f-b63b-aa150bbfff2d)


#### dir /on → nome
```py
dir C:\windows\system32 /on
```
![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/294e604d-d412-4063-bc6a-ffdb99c6c501)

#### dir /oe → extensão
```py
dir C:\windows\system32 /oe
```
![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/a60745ad-38f8-42c6-a178-6f135db3f115)


#### dir /od → data
```py
dir C:\windows\system32 /od
```
![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/dbda7c69-7ff0-4478-8dbf-b4cb487860ae)


#### dir /os → tamanho
```py
dir C:\windows\system32 /os
```
![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/58060e84-489f-4765-928f-5ea129f0f776)

## Arquivos

```py
 nome.extensão
  ↓     ↳ Tipo do arquivo (4 caracteres)
(n caracteres)               .docx
                             .doc
                             .exe

Filtros
 * → N caracteres  *.docx | a*
 ? → 1 Caractere   A??.exe
```

exemplos:

 - busca de arquivo especifico

   ![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/8ce334c4-5493-4d58-b151-2b6dba76d7bc)

 - busca de arquivo geral com uma letra inicial, sem extensão
   
   ![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/82e9c873-a155-4702-b4af-601378ee149e)

 - busca de arquivo geral com uma letra inicial, com extensão
   
   ![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/c3224d94-b4f3-42a3-9556-595a4bc779c2)

 - busca de arquivo geral com uma letra inicial, 1 a 4 caracteres, com todas extensões
   
   ![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/0841070f-c54c-4a10-882f-b1d2e443a99b)


## copy

copiar um arquivo (apenas arquivo)

```py
copy [ORIGEM] ARQUIVOS [DESTINO] [OPÇÕES]
```

![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/da6e93b9-6003-4b38-a4f0-7611f141f224)


#### tree /f | more

procura o arquivo

![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/23c5fb42-5eab-4454-9235-1a9b76a95abc)


#### copy 
