from ex115a import*
from ex115b import*
from time import sleep


nome = 'dadospessoas.txt'

while True: 
    lin('MENU PRINCIPAL')
    print(f'''{cores[3]}1 {cores[0]}- {cores[4]}Ver pessoas cadastradas{cores[0]}
{cores[3]}2{cores[0]} - {cores[4]}Cadastrar nova Pessoa{cores[0]}
{cores[3]}3{cores[0]} - {cores[4]}Sair do Sistema{cores[0]}''')
    print('-' * 45)
    while True:
        try:
            opcao = int(input(f'{cores[3]}Sua Opção: {cores[0]}'))
        except (TypeError, ValueError):
            print(f'{cores[1]}ERRO: por favor digite um número inteiro válido.{cores[0]}')
        except KeyboardInterrupt:
            print(f'{cores[1]}Usuário preferiu não informar a opção.{cores[0]}')
        else:
            sleep(0.5)
            if opcao >= 1 and opcao <= 3:
                break
            else:
                print(f'{cores[1]}ERRO: Digite uma opção válida!{cores[0]}')


    if opcao == 1:
        lin(f'Opção {opcao}')
        opc(nome)
    elif opcao == 2:
        lin('NOVO CADASTRO')
        n = str(input(f'{cores[3]}Nome: {cores[0]}'))
        idade = lerIdade('Idade: ')
        cadastrar(nome, n, idade)
    elif opcao == 3:
        lin('Saindo do sistema... Até logo!')
        break
