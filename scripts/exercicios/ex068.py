from random import randint
cont = 0
print('=-' * 15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 15)
while True:
    r = randint(0, 10)
    n = int(input('Diga um valor: '))
    v = r + n
    s = ' '
    while s not in  'PI':
        s = str(input('Par ou Ímpar ? [I/P] ')).upper()[0]
    print(f'Você jogou {n} e o computador {r}. Total de {v}, ', end='')
    print('\033[1;33mDEU PAR\033[m' if v % 2 == 0 else '\033[1;33;40mDEU IMPAR\033[m')
    if v % 2 == 0 and s == 'P' or v % 2 >= 1 and s == 'I':
        print('\033[1;032mVocê VENCEU!\033[m')
        print('Vamos jogar novamente...')
        cont += 1
    else:
        print('\033[1;31mVocê PERDEU!\033[m')
        break
    print('=-' * 15)
print(f'\033[1;031mGAMER OVER!\033[m Você venceu \033[1;32m{cont}\033[m vezes.')
