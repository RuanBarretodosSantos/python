print('Gerador de PA')
print('==-' * 7)
prim = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
termo = prim
count = 1
total = 0
mais = 10
print('==-' * 7)
while mais != 0:
    total +=  mais
    while count <= total:
        print(termo, end=' ➙  ')
        termo += raz
        count += 1
    print('P A U S A')
    mais = int(input('Quantos termos você quer mostrar a mais ? '))
print('F I M')
