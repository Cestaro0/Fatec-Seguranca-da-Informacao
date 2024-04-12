@echo off

:voltar
cls

set /p A=Digite valor para a variavel A:
if %A% leq 0 (goto :zero) else (goto :fim)

:zero 
echo.
echo valor deve ser maior que zero
echo.
pause
goto :voltar

:fim
echo.
echo volor de A: %A%
echo.