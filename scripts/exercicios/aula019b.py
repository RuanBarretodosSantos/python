pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['peso'] = 99.4
pessoas['nome'] = 'Leandro'
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos.')
for k, v in pessoas.items():
    print(f'O {k} é {v}')
