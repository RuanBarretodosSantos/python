def maior(*num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for n in num:
        print(f'{n}', end=' ')
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(lista)}')


lista = [2, 9, 4, 7, 1]
maior(lista)
lista = [4, 7, 0]
maior(lista)
lista = [1, 2]
maior(lista)
lista = [6]
maior(lista)
lista = [0]
maior(lista)
print()