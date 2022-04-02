principal = [[], []]
cont = 0
for c in range(1, 8):
    valor = int(input(f'Digite o valor {c}°. valor: '))
    if valor % 2 == 0:
        principal[0].append(valor)
    else:
        principal[1].append(valor)
print('-=' * 30)
principal.sort()
print(f'Os valores pares digitados foram: {principal[0]}')
print(f'Os valores ímpares digitados foram: {principal[1]}')