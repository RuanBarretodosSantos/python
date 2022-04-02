menu = 0
enfeite = '=-=' * 7
valor_1 = int(input('Primeiro valor: '))
valor_2 = int(input('Segundo valor: '))
while menu != 6:
    print('[ 1 ] somar \n[ 2 ] multiplicar\n[ 3 ] maior \n[ 4 ] novos números\n[ 5 ] potencia\n[ 6 ] sair do progama')
    menu = int(input('>>>>> Qual é a sua opção ? '))
    if menu == 1:
        soma = valor_1 + valor_2
        print(f'A soma entre {valor_1} + {valor_2} é {soma}') 
    elif menu == 2: 
        multi = valor_1 * valor_2
        print(f'A multiplicação de {valor_1} X {valor_2} é {multi}')
    elif menu == 3:
        if valor_1 != valor_2:
            if valor_1 > valor_2:
                maior = valor_1
                menor = valor_2
            if valor_1 < valor_2:
                maior = valor_2
                menor = valor_1
            print(f'Entre {valor_1} e {valor_2}, o maior é {maior} e o menor é {menor}')
        elif valor_1 == valor_2:
             print(f'Os valores {valor_1} e {valor_2} são iguais')       
    elif menu == 4:
         print('Informe os números novamente:')
         valor_1 = int(input('Primeiro valor: '))
         valor_2 = int(input('Segundo valor: '))
    elif menu == 5:
        escolha = int(input('Você quer que o primeiro ou o segundo valor seja a base ? [1/2] ' ))
        if escolha == 1:
            base = valor_1
            expo = valor_2
            pot = valor_1 ** valor_2
        elif escolha == 2: 
            base = valor_2
            expo = valor_1
            pot = valor_2 ** valor_1
        print(f'O resultado do calculo usando {base} como base, e {expo} como expoente. Teremos o valor da potência igual a {pot}')
    if menu != 6:
        print(enfeite)
print('-==-==- F I M -==-==-')
