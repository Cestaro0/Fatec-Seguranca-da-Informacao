@echo off

:voltar 
pause
cls

echo [ 1 ] Copiar arquivos para S:
echo [ 2 ] Sair do programa

set /p opcao=Digite a opcao:

if %opcao% equ 1 (goto :copia)
if %opcao% equ 2 (goto :sair) else (goto :opcaoInvalida)

:copia 
copy c:\windows\system32\c*.exe s:
dir s:
goto :voltar

:opcaoInvalida
echo Opcao invalida amigao :(
pause
goto :sair

:sair 
echo fim do programa press [ enter ] para continuar. . .
pause
cls
