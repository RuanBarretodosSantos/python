inicio = int(input('Início: '))
numero = int(input('Fim: '))
passo = int(input('Passo: '))
print('-=' * 20)
if passo == 0:
    print('ERRO!')
else:
     for c in range(inicio, numero + 1, passo):
        print(c)
        print('FIM')
print('-=' * 20)
