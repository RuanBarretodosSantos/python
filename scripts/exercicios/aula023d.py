try:
    n = int(input('Numerado: '))
    d = int(input('Denominador: '))
    s = n / d
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
except Exception as error:
    print(f'O erro encontrado foi {error.__cause__}')
else:
    print(f'O resultado de {n} / {d} é {s:.1f}')
finally: 
    print('Volte sempre! Muito obrigado.')
