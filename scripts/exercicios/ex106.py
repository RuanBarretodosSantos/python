while True:
    print('\033[0;37;42m~' * 40)
    print(f'{"SISTEMA DE AJUDA PyHELP":^40}')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[m')
    py = str(input('Função ou Biblioteca > ')).lower()
    if py == 'fim':
        break
    print('\033[37;46m~' * 40)
    junt = 'Acessando o manual do comando ' + py
    print(f'{junt:^40}')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[m')
    help(py)
print('~' * 40)
print(f'{"ATÉ LOGO":^30}')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[m')
