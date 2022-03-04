ano = int(input('Digite o ano escolhido: '))
c = ano // 100 % 10
m = ano // 1000 % 10
if c and m == 0:
    cal = ano % 400
else:
    cal = ano % 4
if cal >=1:
    print('O ano não é bisexto')
else:
    print('O ano é bisexto')