from time import sleep
valor = float(input('Qual o valor do produto ? R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão 
[ 3 ] 2x cartão 
[ 4 ] 3x ou mais no cartão
''')
div = int(input('Qual é a opção ? '))
print('CALCULANDO...')
sleep(1)
if div == 0:
    total = (valor) - valor * 10 / 100 
elif div == 1:
    total = (valor) - valor * 5 / 100
elif div >= 3:
    total = valor + valor * 20 /100
print(f'O valor total a pagar é: {total}')