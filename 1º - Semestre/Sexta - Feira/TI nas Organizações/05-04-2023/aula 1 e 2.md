# Variaveis de memoria


## set
```py
set [OPÇÃO] NOME_VAR=[VALOR]
```

informações adicionais do prompt:
```py
Exibe, define ou remove variáveis de ambiente do cmd.exe.

SET [variável=[cadeia_de_caracteres]]

  variável               Especifica o nome da variável de ambiente.
  cadeia_de_caracteres   Especifica uma série de caracteres a serem atribuídos
                         à variável.

Digite SET sem parâmetros para exibir as variáveis de ambiente atuais.

Se as extensões de comando estiverem ativadas, SET será alterado como a seguir:

O comando SET chamado com apenas um nome de variável, nenhum sinal de igual
ou valor exibirá o valor de todas as variáveis cujo prefixo corresponda ao nome
fornecido ao comando SET. Por exemplo:

    SET P

exibiria todas as variáveis começando com a letra 'P'

O comando SET definirá o ERRORLEVEL como 1 se o nome da variável não for
encontrado no ambiente atual.

O comando SET não permitirá que um sinal de igual seja parte do nome de
uma variável.

Duas novas opções foram adicionadas ao comando SET:

    SET /A expressão
    SET /P variável=[cadeia_do_prompt]

A opção /A especifica que a cadeia de caracteres à direita do sinal de igual
é uma expressão numérica que é avaliada. O avaliador da expressão
é muito simples e dá suporte às seguintes operações, em ordem
decrescente de precedência:

    ()                  - agrupamento
    ! ~ -               - operadores unários
    * / %               - operadores aritméticos
    + -                 - operadores aritméticos
    << >>               - alternância lógica
    &                   - bit a bit E
    ^                   - bit a bit exclusivo OU
    |                   - bit a bit OU
    = *= /= %= += -=    - atribuição
      &= ^= |= <<= >>=
    ,                   - separador de expressões

Se você usar qualquer um dos operadores lógicos ou de módulo, precisará
colocar a cadeia de caracteres da expressão entre aspas. Qualquer
cadeia de caracteres não numérica na expressão é tratada como nomes
de variável de ambiente cujos valores são convertidos para números antes
de serem usados. Se um nome de variável de ambiente for especificado,
mas não estiver definido no ambiente atual, será usado um valor de zero.
Isso permite fazer aritmética com valores de variáveis de ambiente, sem ter de
digitar todos esses sinais de % para obter os valores. Se SET /A
for executado a partir da linha de comando fora de um script de comando,
ele exibirá o valor final da expressão. O operador de atribuição requer um
nome de variável de ambiente à sua esquerda. Os valores numéricos
são valores decimais, a menos que sejam antecedidos por 0x para números
hexadecimais e 0 para números octais. Portanto, 0x12 é o mesmo que 18
e o mesmo que 022. Observe que a notação octal pode causar confusão: 08 e 09
não são números válidos porque 8 e
9 não são dígitos octais válidos.

A opção /P permite definir o valor de uma variável para uma linha de entrada
digitada pelo usuário. Exibe a cadeia de caracteres do prompt especificada
antes de ler a linha de entrada. A cadeia de caracteres do prompt pode estar
vazia.

A substituição da variável de ambiente foi aprimorada da seguinte forma:

    %PATH:seq1=seq2%

expandiria a variável de ambiente PATH, substituindo cada ocorrência de
"seq1" no resultado expandido por "seq2". "Seq2" pode ser a cadeia de
caracteres vazia para excluir efetivamente todas as ocorrências de "seq1" da
saída expandida. "seq1" pode começar com um asterisco e, neste caso,
corresponderia a tudo desde o início da saída expandida até a primeira
ocorrência da parte restante de seq1.

Também pode especificar subcadeias de caracteres para uma expansão.

    %PATH:~10,5%

expandiria a variável de ambiente PATH e usaria apenas os 5 caracteres
que começassem no caractere 11 (deslocamento 10) do resultado expandido.
Se o comprimento não for especificado, será padronizado como o restante
do valor da variável. Se qualquer um dos números
(deslocamento ou comprimento) for negativo, o número usado será o comprimento
do valor da variável de ambiente adicionado ao deslocamento ou comprimento
especificado.

    %PATH:~-10%

extrairia os últimos 10 da variável PATH.

    %PATH:~0,-2%

extrairia todos os caracteres da variável PATH, com exceção dos 2 últimos.

Finalmente, foi adicionado o suporte à expansão de variáveis de ambiente
atrasada. Esse suporte está sempre desativado por padrão, mas pode ser
ativado/desativado através da opção da linha de comando /V do CMD.EXE.
Consulte CMD /?

A expansão de variáveis de ambiente atrasada é útil para contornar
as limitações da expansão atual que ocorre quando uma linha
de texto é lida, e não quando é executada. O exemplo a seguir
demonstra o problema com a expansão de variável imediata:

    set VAR=antes
    if "%VAR%" == "antes" (
        set VAR=depois
        if "%VAR%" == "depois" @echo Se você ler isto, terá funcionado
    )

nunca exibiria a mensagem, já que %VAR% em AMBAS as instruções IF
é substituído quando a primeira instrução IF é lida, pois inclui
logicamente o corpo do IF, que é uma instrução composta. Portanto, o
IF dentro da instrução composta está realmente comparando "antes" com
"depois", que nunca será igual. Da mesma forma, o exemplo a seguir
não funcionará como esperado:

    set LIST=
    for %i in (*) do set LIST=%LIST% %i
    echo %LIST%

porque NÃO criará uma lista de arquivos na pasta atual mas,
em vez disso, apenas definirá a variável LIST como o último arquivo encontrado.
Novamente, isso ocorre porque a %LIST% é expandida apenas uma vez
quando a instrução FOR é lida, e nesse momento a variável LIST está vazia.
Portanto, o loop FOR que está de fato sendo executado é:

    for %i in (*) do set LIST= %i

que apenas continua definindo LIST como o último arquivo encontrado.

A expansão de variáveis de ambiente atrasada permite usar um caractere
diferente (o ponto de exclamação) para expandir variáveis de ambiente no
tempo de execução. Se a expansão de variáveis atrasada estiver ativada,
os exemplos acima poderão ser escritos da seguinte forma para funcionar
como o desejado:

    set VAR=antes
    if "%VAR%" == "antes" (
        set VAR=depois
        if "!VAR!" == "depois" @echo Se você ler isto, terá funcionado
    )

    set LIST=
    for %i in (*) do set LIST=!LIST! %i
    echo %LIST%

Se as extensões de comando estiverem ativadas, haverá diversas variáveis
de ambiente dinâmicas que poderão ser expandidas, mas que não aparecerão na
lista de variáveis exibida pelo SET. Esses valores de variáveis são
computados dinamicamente sempre que o valor da variável é expandido.
Se o usuário definir explicitamente uma variável com um desses nomes,
essa definição substituirá a definição dinâmica descrita abaixo:

%CD% - expande para a cadeia de caracteres da pasta atual.

%DATE% - expande para a data atual usando o mesmo formato que o comando DATE.

%TIME% - expande para a hora atual usando o mesmo formato que o comando TIME.

%RANDOM% - expande para um número decimal aleatório entre 0 e 32767.

%ERRORLEVEL% - expande para o valor ERRORLEVEL atual

%CMDEXTVERSION% - expande para o número da versão das extensões do
    processador de comandos atual.

%CMDCMDLINE% - expande para a linha de comando original que chamou o
    processador de comandos.

%HIGHESTNUMANODENUMBER% - expande para o número de nó NUMA mais alto
    nesta máquina.

```


## /p

Cria a variavel vazia

```py
set /p nome=Digite o rg:
```
exemplo de utilização de variavel em prompt:

![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/5ae0f94a-a336-4a08-987f-3caef89df95a)

