from datetime import date
maior = 0
menor = 0
for pessoas in range(1, 8):
    ano = int(input(f'Em que ano a {pessoas}ª pessoa nasceu ? '))
    if date.today().year - ano  >= 21:
        maior += 1
    else:
        menor += 1
print(f'Ao todos tivemos {maior} maiores de idade')
print(f'E também tivemos tivemos {menor} pessoas menores de idade')