from datetime import date
nascimento = int(input('Que ano você nasceu ? '))
atual = date.today().year - nascimento
alistamento = nascimento + 18
if atual == 18:
    print(f'já está na hora de você se alistar!')
elif atual < 18:
    print(f'Você não tem a idade minima para se alistar! Seu alistamento será em {alistamento}')
else:
    print(f'Seu tempo de se alistar já passou!')
    print(f'Você deveria ter se alistado em {alistamento}, Há {date.today().year - alistamento} anos atrás')

print('Muito obrigado por usar nossos serviços, tenha um bom dia! ')