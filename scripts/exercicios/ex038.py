print('-=' * 20)
valor1 = int(input('Primeiro número: '))
valor2 = int(input('Segundo número: '))
print('-=' * 20)
if valor1 > valor2:
    print(f'O primeiro valor ({valor1}) é maior que o segundo ({valor2})')
elif valor2 > valor1:
    print(f'O segundo valor ({valor2}) é maior que o primeiro ({valor1})')
else:                                        
    print('Não existe valor maior, os dois são iguais!')

