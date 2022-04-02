media = 0
maior = 0
nom = ''
mulher = 0
for grupo in range(1, 5):
    print(f'----- {grupo}ª -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    media += idade / 4 
    if grupo == 1 and sexo == 'M':
        maior = idade
        nom = nome
    if sexo == 'M' and idade > maior:
        maior = idade
        nom = nome
    if sexo == 'F' and idade < 20:
        mulher += 1
print(f'A média de idade do grupo é {media} anos')
print(f'O homem mais velho tem {maior} anos e se chama {nome}')
print(f'Ao todo são {mulher} mulheres com menos de 20 anos')