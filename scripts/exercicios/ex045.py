from random import choice
escolha = str(input('Escolha com o que você vai jogar: ')).strip().capitalize()
lista = ['Pedra', 'Papel', 'Tesoura']
sorteio = choice(lista)
if escolha == 'Pedra' and sorteio == 'Papel' or escolha == 'Tesoura' and sorteio == 'Pedra' or  escolha == 'Papel' and sorteio == 'Tesoura':
    print(f'Você perdeu! O computador escolheu {sorteio}')
elif escolha == 'Tesoura' and sorteio == 'Papel' or escolha == 'Pedra' and sorteio == 'Tesoura' and escolha == 'Papel' and sorteio == 'Pedra':
    print(f'Você ganhou! O computador escolheu {sorteio}')
elif escolha == sorteio:
    print('Deu empate! Jogue novamente!')
elif escolha != lista:
    print('Algo deu errado, tente novamente!')