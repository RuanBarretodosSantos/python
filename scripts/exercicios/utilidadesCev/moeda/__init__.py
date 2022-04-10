def aumentar(n=0, taxa=0, formato=False):
    res = n + (n * taxa/100)
    return res if formato is False else moeda(res)
    

def diminuir(n=0, taxa=0, format=False):
    res = n - (n * taxa/100)
    return res if format is False else moeda(res)


def dobro(n=0, formato=False):
    res = n * 2
    return res if formato is False else moeda(res)


def metade(n=0, formato=False):
    res = n / 2
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(a = 0, b=0, c=0):
    print('-' * 45)
    print(f'{"RESUMO DO VALOR".center(45)}')
    print('-' * 45)
    print(f'Preço analisado: \t{moeda(a)}')
    print(f'Dobro do preço: \t{dobro(a , True)}')
    print(f'Metade do preço: \t{metade(a, True)}')
    print(f'{b}% de aumento: \t{aumentar(a, b, True)}')
    print(f'{c}% de redução: \t{diminuir(a, c, True)}')
    print('-' * 45)