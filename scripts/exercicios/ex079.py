num = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor not in num:
        print('Valor adicionado com sucesso...')
        num.append(valor)
    else:
        print('Valor duplicado! Não vou adcionar...')
    while True:
        res = str(input('Quer continuar ? [S/N] ')).upper().strip()[0] 
        if 'S' in res or 'N' in res:
            break 
    if 'N' in res:
        break
num.sort()
print(f'Você digitou: \033[1;32m{num}\033[m')
print(f'O maior número digitado foi: \033[1;32m{max(num)}\033[m')
print(f'O menor número digitado foi: \033[1;32m{min(num)}\033[m')
