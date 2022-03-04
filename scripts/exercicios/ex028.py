from random import randint
sorteio = randint(0, 5) #Faz o computador "PENSAR" 
enfeite = '-=--=' * 20
print(enfeite)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print(enfeite)
entrada = int(input('Em que número eu pensei ?  ')) #Entrada de dados (onde o jogador tenta advinhar)
print('PROCESSANDO...')
if sorteio == entrada: #Condição
    print('Você acertou!')
else:
    print('Você errou!')
print(f'O número sorteado foi: {sorteio}') #