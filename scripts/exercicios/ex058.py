from random import randint
count = 1
sorteio = randint(0, 10)
print('Acabei de pensar em um número entre \033[0;33;40m 0 e 10\033[m.')
res = int(input('Será que você consegue adivinhar qual foi ? '))
while not res == sorteio:
    if res < sorteio:
        res = int(input('\033[0;31;40mMais...\033[mTente mais uma vez. \nQual é o seu palpite ? '))
        count += 1
    elif res > sorteio:
        res = int(input('\033[0;31;40mMenos...\033[m Tente mais uma vez. \nQual é o seu palpite ? ')) 
        count += 1
if count <=  3:
    print(f'Acertou com \033[0;32;40m{count}\033[m tentativas. Parabéns')
elif count > 4:
    print(f'Você acertou com \033[0;32;40m{count}\033[m tentativas. Dá pra melhorar...')