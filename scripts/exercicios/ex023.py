numero = int(input('Digite um número de quatro digitos: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f'Analisando o número {numero}')
print('Unidade: ', u)
print('Dezena:  ', d)
print('Centena: ', c)
print('milhar:  ', m)

