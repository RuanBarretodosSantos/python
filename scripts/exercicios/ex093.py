dados = {}
lista = []
total = 0
dados['nome'] = str(input('Nome do jogador: ')).strip().title()
part = int(input(f' Quantas partidas {dados["nome"]} jogou ? '))
for c in range(0 , part):
    gol = int(input(f'   Quantos gols na partida {c} ? '))
    total += gol 
    lista.append(gol)
dados['gols'] = lista
dados['total'] = total  
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
for c, v in enumerate(lista):
    print(f'   => Na partida {c}, fez {v} gols.')
print(f'Foi um total de {dados["total"]}.')
print()