#Leia um angulo em radianos e apresente-o convertido em graus. A f ˆ ormula de convers ´ ao˜
#e: ´ G = R ∗ 180/π, sendo G o angulo em graus e ˆ R em radianos e π = 3.14.
import math

def radianoToAngulo(A):
    return A * 180 / math.pi    

if __name__ == '__main__':
    n = float(input('Digite um radiano:'))
    print('a conversao do radiano para angulo e:', radianoToAngulo(n))