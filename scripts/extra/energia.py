from time import sleep
from sistema import*


while True:
    Menu()
    esc = int(input('Opção: '))
    if esc == 1:
        sleep(0.5)
        EnergiaCinetica()
    elif esc == 2:
        sleep(0.5)
        EnergiaElas()
    elif esc == 3:
        sleep(0.5)
        EnergiaPot()
    elif esc == 4:
        sleep(0.5) 
        Linhas('Saindo do sistema...Até mais!')
        break 

    else:
        print(f'{esc} não é uma opção.')