@echo off
rem verificando se um arquivo existe, se existir liste ele

rem if exist calc.exe (dir calc.exe) else (echo arquivo nao encontrado!)

rem verificando com not

if not exist calc.exe (echo arquivo nao encontrado) else (echo dir calc.exe)
