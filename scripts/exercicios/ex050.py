from itertools import count


soma = 0
count_par = 0
count = 0 
for par in range(0, 6):
    pares = int(input('Digite um número: '))
    count = count + 1
    if pares % 2 == 0:
        count_par = 0 + 1
        soma = soma + pares
print(f'Você informou 6 números, {count_par} número(s) é/são par. A soma dos pares é {soma}')

