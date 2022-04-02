lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(f'A variavel tem {len(lanche)} lanches')
for comida in lanche:
    print(f'Esses são os lanches: {comida}')
for cont in range(0, len(lanche)):
    print(f'Esses são os lanches: {lanche[cont]}')
for pos, comida in enumerate(lanche):
    print(f'Esse lanche {comida} está na posição {pos}')
print('São muitos lanches!')