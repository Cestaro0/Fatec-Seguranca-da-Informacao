@echo off
rem verfica se existe o calc.exe, se existir, apaga, se não apaga

if exist calc.exe (goto :apaga) else (goto :copia)

:apaga
del calc.exe
echo arquivo deletado
pause 
goto :fim

:copia
copy c:\windows\system32\c*.exe s:
dir s:
pause

:fim
echo fim do programa!!!
cls