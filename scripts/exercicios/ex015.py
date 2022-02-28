dia = int(input('Quantos dias alugado ? '))
km = int(input('Quantos KMs foram rodados ? '))
pago = (dia * 60) + (km * 0.15)
print(f'Você dirigiu por {km} KMs, por {dia} dias. O valor total a pagar é R${pago}')