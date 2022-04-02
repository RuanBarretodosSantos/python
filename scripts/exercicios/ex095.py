time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'     Quantos gols na partida {c} ? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        res = str(input('Quer continuar ? [S/N] ')).upper().strip()[0]
        if res in 'SN':
            break
    if res == 'N':
        break 
print('-=' * 30) 
print('cod', end='') 
for i in jogador.keys():
  print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('-=' * 30)
while True:
    per = int(input('Mostrae dados de qual jogador ? (999 Para parar) '))
    if per == 999:
        break
    if per >= len(time):
        print(f'ERRO! Não existe jogador com código {per}!')
    else:
        (f'  -- LEVANTAMENTO DO JOGADOR {time[per]["nome"]}:')
        for i, g, in enumerate(time[per]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 30)
print('<< VOLTE SEMPRE! >>')