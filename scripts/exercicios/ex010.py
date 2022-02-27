from lib2to3.pgen2.token import DOUBLESTAR
from ntpath import realpath


real =  float(input('Quantos reais você tem ? '))  
dolar = float(input('Qual é o valor do dolar ? '))
cal = real / dolar
print('Com {} você consegue comprar {} dólares'.format(real, dolar))