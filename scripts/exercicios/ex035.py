from time import sleep
print('-=' *20)
print('Analisador de Triângulos')
print('-=' *20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segmento segmento: '))
r3 = float(input('Terceiro segmento: '))
print('CALCULANDO...')
sleep(1)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possivel formar um triangulo')
else:
    print('Não é possivel formar um triangulo')