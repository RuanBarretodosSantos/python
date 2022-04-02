num = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
decimo = num + (10 - 1) * raz
for cal in range(num, decimo + raz, raz):
    print(cal, end=' ➙ ')
print('ACABOU')