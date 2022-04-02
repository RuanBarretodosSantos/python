n = 0
soma = 0
s = 0
stri = ''
while True:
    n = int(input('Digite um número: '))
    s += 1
    soma += n 
    stri = str(input('Você quer continuar ? [S/N] ')).upper().strip()[0]
    if stri == 'N':
        break
print(f'Você digitou {s} números, a soma foi {soma}')