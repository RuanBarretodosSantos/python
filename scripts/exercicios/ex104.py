def leiaInt(txt):
    while True:
        r = str(input(txt)).strip()
        if r.isnumeric():
            int(r)
            return r
            break
        else:
            print('\033[1;31mERRO! Digite um número válido.\033[m')
            


#PROGAMA PRINCIPAL
print('-' * 30)
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
