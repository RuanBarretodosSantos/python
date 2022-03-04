n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = (n1 + n2 + n3) / 3
if media >=5:
    print('Parabéns, você passou!')
else:
    print('Infelizemnte você não passou')
print(f'A sua média foi: {media:.2f}')