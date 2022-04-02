frase = str(input('Digite  uma frase: ')).strip().upper()
palavras = frase.split(
)
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if junto == inverso:
    print('Temos um palíndromo aqui')
else:
    print(f'{junto} não é um palíndomo')