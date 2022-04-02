from time import sleep


def contador(inc, fim, passo):
    for c in range(inc, fim, passo):
        print(f'{c}', end=' ')
    print(fim, end=' ')
    print('FIM!')


def lin():
    print('-=' * 30)


lin()
print(f'Contagem de 1 até 10 de 1 em 1')
contador(0, 10, 1)
lin()
print(f'Contagem de 10 até 0 de 2 em 2')
contador(10, 0, -2)
lin()
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
