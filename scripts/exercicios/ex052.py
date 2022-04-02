count = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):

    if num % c == 0: 
        count += 1
        print(f'\033[32m {c} \033[m', end=' ')
       
    else:
        print(f'\033[31m {c} \033[m', end=' ') 
if count > 2:
    print(f'O número {num} não é primo, ele pode ser divido por {count} números')
elif count <= 2:
    print(f'O número {num} é primo')