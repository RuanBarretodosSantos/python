try:
    n = int(input('Numerado: '))
    d = int(input('Denominador: '))
    s = n / d
except Exception as erro:
    print(f'O problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado de {n} / {d} é {s}')
finally: 
    print('Volte sempre! Muito obrigado.')
