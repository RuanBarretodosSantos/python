from ex115a  import*

def lin(msg):
    print('-' * 45)
    print(f'{msg.center(45)}')
    print('-' * 45)


def ArquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def CriarArquivo(nome):
    try:
        open(nome, 'wt+')
    except FileNotFoundError:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def LerDados(nome):
    try:
        a = open(nome, 'rt')   
    except FileExistsError():
        print(f'Tivemos um erro ao tentar ler o arquivo {nome}')
    else:
        lin('PESSOAS CADASTRADAS')
        print(a.read())
    finally:
        a.close()


def cadastrar(nome, n = 'desconhecido', idade = 0):
    try:
        a = open(nome, 'at')
    except:
        print('Houve um problema na arbetura do arquivo!')
    else:
        a.write(f'{n:<30}{idade:>3} anos\n')
    finally:
        a.close()
