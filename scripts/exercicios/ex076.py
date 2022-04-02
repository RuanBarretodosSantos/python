lista = ('Lápis', 1.75, 'Borracha',  2.00,'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Caompasso', 99.9, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 30)
print('{:^30}'.format('LISTAGEM DE PREÇOS'))
print('-' * 30)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R$ {lista[pos]:>10}')
print('-' * 30)