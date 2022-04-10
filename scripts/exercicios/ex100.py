from random import randint
from time import sleep


def sorteio(res):
    for c in range(0, 5):
        res.append(randint(0, 9))
    print('Sorteando 5 valores da lista: ', end='')
    for v in res:
        print(f'{v}', end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')


def pares(par):
    soma = 0
    for c in par:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {lista}, temos {soma}')


lista = []
sorteio(lista)
pares(lista)
