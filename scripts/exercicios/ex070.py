total = mil = barato = cont = 0
result = ''
print('-' * 30)
print('LOJA SUPER BARATÃO')
print('-' * 30)
while True:
    nome = str(input('Nome do produto: ')).strip().title()
    valor = float(input('Valor do produto: R$  '))
    total += valor
    cont += 1
    if cont == 1 or barato > valor:
        barato = valor
        result = nome
    if valor > 1000:
        mil += 1
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar ? [S/N] ')).upper().strip()
    if res == 'N':
        break
print('------------ FIM DO PROGAMA ------------')
print(f'O total de compra foi {total:.2f}')
print(f'Temos {mil} produtos custando mais de R$ 1000.00' if mil > 1 or mil == 0 else f'Temos {mil} produto custando mais de R$ 1000.00')
print(f'O produto mais barato foi {result} que custa R$ {barato:.2f}')
