salario = float(input('Digite o salario: '))
if salario >= 1250.00:
    porcentagem = salario * 10 / 100
    print(f'O novo salario com o aumento de {porcentagem} é {porcentagem + salario}')
else: 
    porcentagem = salario * 15 / 100
    print(f'O seu novo salario com aumento de {porcentagem} é {porcentagem + salario} ')