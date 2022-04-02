def area(larg, comp):
    s = larg * comp
    print(f'A área de um terreno de {b} X {h} é {s}m²')


#Progama Principal
print(f'{"Controle de Terrenos":^30}')
print('-' * 30)
b = float(input('Largura (m): '))
h = float(input('Altura (m): '))
area(b, h)