aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 5:
    aluno['Situacao'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
for c, v in aluno.items():
    print(f'{c} é igual a {v}')