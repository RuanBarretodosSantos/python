sal = float(input('Qual o seu salário ? '))
por = float(input('Qual a porcentagem do aumento ? '))
va2 = 100
ca1 = por / va2
print(ca1)
ca2 = sal * ca1
total = sal + ca2 
print('O seu salario atual é R${}. Com o aumento de {}% (R${}), irá ficar: R${}'.format(sal,por, ca2, total))