soma = 0
cont = 0
for num in range(1, 500, 2):
    if num % 3 ==0:
        cont = cont + 1
        soma = soma + num
print(f'A soma de {cont} valores solicitados é {soma}')