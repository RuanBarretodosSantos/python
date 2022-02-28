from email.utils import collapse_rfc2231_value


real =  float(input('Quantos reais você tem ? R$ '))  
dolar = real / 5.16
euro = real / 5.77
print(f'Com {real} você consegue comprar {dolar:.2f} dólares ou {euro:.2f}')