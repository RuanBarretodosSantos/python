def Linhas(msg):
    print('-' * 45)
    print(msg.center(45))
    print('-' * 45)


def Menu():
    Linhas('OPÇÕES')
    print('''1 - Enercia cinética
2 - Energia potencial elástica
3 - Energia potencial gravitacional
4 - Sair do sistema''')
    print('-' * 45)
    

def EnergiaCinetica():
    Linhas('Energia Cinética')
    massa = float(input('Massa [KG]: '))
    veloc = float(input('Velocidade [M/s]: '))
    calculo = massa * (veloc * veloc) / 2
    print(f'{calculo} J')


def EnergiaElas():
    Linhas('Energia potencial gravitacional')
    const = float(input('Constante: '))
    varia = float(input('Variação: '))
    calculo = const * (varia * varia) / 2
    print(f'{calculo} J')


def EnergiaPot():
    Linhas('Energia potencial elástica')
    massa = float(input('Massa [KG]: '))
    gravi = float(input('Gravidade [M/s]: '))
    altur = float(input('Altura [M]: '))
    calculo = massa * gravi * altur
    print(f'{calculo} J')