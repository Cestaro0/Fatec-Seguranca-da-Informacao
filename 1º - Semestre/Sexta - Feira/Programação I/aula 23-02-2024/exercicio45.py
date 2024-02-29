#Fac¸a um programa para converter uma letra maiuscula em letra min ´ uscula. Use a tabela ´
#ASCII para resolver o problema.


if __name__ == '__main__':
    anyChar = input('digite uma letra minuscula:')
    print("a letra minuscula e: %s" %chr(ord(anyChar) - 32))
    anyChar = input('digite uma letra maiscula:')
    print("a letra minuscula e: %s" %chr(ord(anyChar) + 32))
    
    
    