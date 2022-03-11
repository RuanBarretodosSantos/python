num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[1] Coverter para BINÁRIO
[2] Coverter para  OCTAL
[3] Coverter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2::]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAl é igual a {oct(num) [2::]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)}')
else:
    print('Opção invalida. Tente novamente')
