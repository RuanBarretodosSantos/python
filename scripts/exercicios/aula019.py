dados = {'nome':'Pedro', 'idade':25}
dados['sexo'] = 'M'
print(dados.values())
print(dados.keys())
print('-=' * 30)
for k, v in dados.items():
    print(f'O {k} é {v}')