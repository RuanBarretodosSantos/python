from time import sleep


def contador(i, f, p):
    """
    Faz uma string e mostra na tela.
    I: Inío da contagem
    F: Fim da contagem
    P: Passo da contagem
    Return: Sem return
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ', flush=True)
        sleep(0.3)
        c += p
    print('FIM!')


contador(0, 100, 10)
help(contador)