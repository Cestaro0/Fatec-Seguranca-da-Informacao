@echo off
rem usando defined agora para ver se a variavel está criada
if defined (echo o nome e %nome%) else (echo variavel nao encontrada!!!)
rem usando not defined, para verificar se está valida
if not defined cidade (echo variavel nao definida!!!) else (echo a cidade e %cidade%)
