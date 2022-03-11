valor = float(input('Qual é o valor da casa ? '))
salario = float(input('Qual é salario do comprador ? '))
prestacao = int(input('Você quer dividir em quantas prestacões ? '))
valor_mes = valor / prestacao / 12
trinta = salario * 30 / 100 
print(f'A prestação será de \033[00;32;40m R$ {valor_mes:.2f} \033[m por mês')
if valor_mes > trinta:
    print('O valor do empréstimo é maior que 30% do seu salario, então seu pedido foi negado!')
else:
    print('O empréstimo foi aprovado!')
  