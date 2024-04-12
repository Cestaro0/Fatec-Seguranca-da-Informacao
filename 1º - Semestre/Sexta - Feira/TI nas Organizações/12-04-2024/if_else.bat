rem primeiro programa: Verifica se o nome é Ana, se for, printa "oi Aninha" se não, Printa o nome digitado

@echo off
set /p nome=Digite o nome:

if %nome% equ Ana (echo Oi Aninha) else (echo oi %nome%)
