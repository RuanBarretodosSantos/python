distancia = float(input('Digite a distancia: '))
print(f'Você está preste a iniciar uma viagem de {distancia} KM')
if distancia >= 200:
    preco = distancia * 0.45
else:
    preco = distancia * 0.50
print(f'O valor da passasgem é R${preco:.2f}')
