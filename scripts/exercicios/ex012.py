preco = float(input('Qual o valor do produto ? R$ '))
porcentagem = float(input('Qual a porcentagem ? '))
calculo = preco - (preco * porcentagem / 100)
print(f'O produto que custava R${preco}, na promoção com desconto de {porcentagem}% vai custar {calculo:.2f}')