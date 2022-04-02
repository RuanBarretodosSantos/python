homens = mulher = maior = 0
while True:
    print('-' * 30)
    print('\033[1;33mCADASTRE UMA PESSOA\033[m')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [\033[1;34mM\033[m/\033[1;35mF\033[m] ')).strip().upper()[0]
    print('-' * 30)
    if idade > 18:
        maior += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    if sexo == 'M':
        homens += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('\033[1;33mQuer continuar ? \033[1;33 [\033[1;32mS\033[m/\033[1;31mN\033[m] ')).upper().strip()[0]
    if opcao == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homens} homens cadrastado')
print(f'E temos {mulher} mulheres com menos de 20 anos')