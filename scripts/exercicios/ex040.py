nota_1 = float(input('Qual foi a primeira nota ? '))
nota_2 = float(input('Qual a segunda nota ? '))
media = (nota_1 + nota_2) / 2
if media < 5:
    print(f'Você foi reprovado! Sua média foi {media:.2f}!')
elif media >= 5 and media <=6.9:
    print(f'Você está de recuperação! Sua média foi {media:.2f}!')
elif media >= 7:
    print(f'Parabéns, você foi aprovado(a)!, Sua média é {media:.2f}!')