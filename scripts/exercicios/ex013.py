sal = float(input('Qual o seu salário ? R$ '))
por = float(input('Qual a porcentagem do aumento ? '))
calculo = sal * por / 100
total = sal + calculo 
print(f'O seu salario atual é R${sal}. Com o aumento de {por}% (R${calculo:.2f}), irá ficar: R${total:.2f}')