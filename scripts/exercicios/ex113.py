def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mUsuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return n 


def leiaReal(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mUsuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return n


num = leiaInt('Digite um inteiro: ')      
real = leiaReal('Digite um valor Real: ') 
print(f'O valor inteiro digitado foi {num} e o real foi {real}')
