cont = 3 
t1 = 0
t2 = 1
print('-----' * 12)
print('Sequência de Fibonacci')
print('-----' * 12)
valor = int(input('Quantos termos você quer mostrar ? '))
print('~~~~~' * 12)
print(f'{t1} ➙  {t2} ' , end='➙ ')
while cont <= valor:
    t3 = t1 + t2
    print(f' {t3}', end=' ➙ ')
    t1 = t2
    t2 = t3
    t3 = t1
    cont += 1  
print(' F I M')
