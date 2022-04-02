maior = menor = soma =  cont = 0
string = 'S'
while string == 'S':
    valor = int(input('Digite um valor: '))
    soma += valor
    cont += 1  
    string = str(input('Quer continuar ? [S/N] ')).upper()[0]
    if cont == 1:
        maior = menot = valor
    else:
        if valor > maior:
            maior = valor
        if valor < maior:
            menor = valor
media = soma / cont
print(f'Você digitou {cont} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
