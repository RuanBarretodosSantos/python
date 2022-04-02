pessoas = list()
temp = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    pessoas.append(temp[:])       
    temp.clear()
    res = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if 'N' in res:
        break
print('=-' * 30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {mai}. Peso de ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'{p[0]}')
print(f'O menor peso foi de {men}. Peso de ', end='')
for p in pessoas:
    if p[1] == men:
        print(f'{p[0]}')
