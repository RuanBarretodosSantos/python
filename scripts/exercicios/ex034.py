salario = float(input('Digite o salario: R$ '))
if salario <= 1250.00:
    porcentagem = salario * 15 / 100
    print(f'O seu novo salario com aumento de {porcentagem:.2f} é {porcentagem + salario:.2f} ')
else: 
    porcentagem = salario * 10 / 100
    print(f'O novo salario com o aumento de {porcentagem:.2f} é {porcentagem + salario:.2f}')