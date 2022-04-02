from turtle import pen


valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
valores.sort(reverse=True)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei {v}')
print(f'Cheguei ao fim da lista.')