pessoas = {}
galera = []
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if 'M' in pessoas['sexo'] or 'F' in pessoas['sexo']:
            break
        print('ERRO! Por favor, digite M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    galera.append(pessoas.copy())
    soma += pessoas['idade']
    while True:
        res = str(input('Quer continuar ? [S/N]: ')).upper().strip()[0]
        if 'S' in res or 'N' in res:
            break
    if 'N' in res:
        break
media = soma / len(galera)
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadrastada.')
print(f'B) A média de idade é {media:5.2f} anos')
print(f'C) As mulheres cadrastada foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print('D) Lista de pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] > media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
print()