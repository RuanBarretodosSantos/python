num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'onze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'vinte')

while True:
    while True:
        esc = int(input('Digite um número entre 0 e 20: '))
        if 0 <= esc <= 20:
            break
        else:
            print('Tente novamente. ', end='')     
    print(f'Você digitou o número {num[esc]}')
    while True:
        des = str(input('Você quer ir de novo ? [S/N] ')).upper()[0]
        if des ==  'N' or des == 'S':
             break
    if des == 'N':
        break
print('--- FIM DO PROGAMA ---')