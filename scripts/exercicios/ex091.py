from operator import itemgetter
from random import randint
from time import sleep
jogo = {'Jogador1': randint(0, 6),
         'Jogador2': randint(0, 6),
         'Jogador3': randint(0, 6),
         'Jogador4': randint(0, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'  {i+1}º lugar: {v[0]} pontos')
    sleep(1)