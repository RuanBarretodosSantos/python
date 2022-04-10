def fatorial(a, show = False):
    """
    -> Lê o fatorial
    a = Número que irá ver o fator
    show = Mostrar o calculo ou não
    """
    f = 1
    for c in range(a, 0, -1):
        f *= c
        
        if show == True:
            print(f'{c}', end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
    print(f)


#PROGAMA PRINCIPAL
fatorial(5, show = True)