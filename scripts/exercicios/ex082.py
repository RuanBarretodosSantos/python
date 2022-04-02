completa = []
par = []
impar = []
while True:
    valor = int(input('Digite um valor: '))
    completa.append(valor)
    if valor % 2 == 0:
         par.append(valor)
    else:
        impar.append(valor)
    while True:
        res =  str(input('Você quer continuar ? [S/N] ')).upper().strip()[0]
        if 'S' or 'N' in res:
            break
    if 'N' in res:
        break
print('-=' * 20)
print(f'A lista completa é {completa}')
print(f'A lista de pares é {par}')
print(f'A lista de núemros ípares é {impar}')
