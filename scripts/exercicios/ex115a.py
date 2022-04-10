from ex115b import*


cores = (
    '\033[0;00m', #Vazio    [0]
    '\033[0;31m', #Vermelho [1] 
    '\033[0;32m', #Verde    [2] 
    '\033[0;33m', #Amarelo  [3]
    '\033[0;34m', #Azul     [4]
    '\033[0;35m', #Rosa     [5]
    '\033[0;36m', #Ciano    [6]
    '\033[0;37m', #Branco   [7]
    )


def lin(msg):
    print('-' * 45)
    print(f'{msg.center(45)}')
    print('-' * 45)


def opc(nome):
    if not ArquivoExiste(nome):
        CriarArquivo(nome)
    else:
        LerDados(nome)

def lerIdade(msg):
    while True:
        try:   
            idade = int(input(f'{cores[3]}{msg} {cores[0]}'))
        except:
            print(f'{cores[1]}ERRO: Tivemos um erro ao cadastrar a idade{cores[0]}')
        else:
            return idade
            break
    
