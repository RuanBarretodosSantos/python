from random import randint
from time import sleep
jogos = list()
lista = []
print('-' * 30)
print('{:^30}'.format('JOGO NA MEGA SENA'))
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie ? '))
print(f'-=-=-=   SORTEANDO {quant} JOGOS  -=-=-=' )
total = 1
while total <= quant:
    cont =  0
    while True:
        num = randint(1, 60)
        if num not in jogos:
            jogos.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.sort()
    lista.append(jogos[:])
    jogos.clear()
    total += 1
for i, l in enumerate(lista):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print(f'-=' * 5, 'BOA SORTE', '-=' * 5)
