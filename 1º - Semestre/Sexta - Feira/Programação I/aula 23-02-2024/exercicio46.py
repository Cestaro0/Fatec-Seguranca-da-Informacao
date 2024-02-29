
if __name__ == '__main__':
    n = int(input('digite o numero:'))
    c = int(n / 100)
    d = int(n % 100 / 10)
    u = int(n % 100 % 10)
     
    res = u * 100 + d * 10 + c
    
    print("%03d" %res)
    
    
    
        
