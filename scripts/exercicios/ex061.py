print('Gerador de PA')
print('==-' * 7)
prim = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
count = 0
termo = prim
print('==-' * 7)
while count != 10:
    print(termo, end=' ➙  ')
    termo += raz
    count += 1
print('F I M')
