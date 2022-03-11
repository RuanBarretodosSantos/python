from datetime import date
anos = int(input('Em qual ano você nasceu ? '))
idade = date.today().year - anos
if idade <= 9:
    print(f'A sua categoria é MIRIM, porquê você tem {idade} anos')
elif idade >= 10 and idade <= 14:
    print(f'A sua categoria é a INFANTIL, porquê você tem {idade} anos')
elif idade >= 15 and idade <= 19:
    print(f'A sua categoria é JUNIOR, porquê você tem {idade} anos')
elif idade == 20:
    print(f'A sua categoria é SÊNIOR, porquê você tem {idade} anos')
elif idade > 20:
    print(f'A sua categoria é MASTER, porquê você tem {idade} anos')