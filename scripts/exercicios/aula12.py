nome = str(input('Qual é seu nome ? ')).strip()
maiusculo = nome.capitalize()
em = 'Ruan' in maiusculo
if em == True:
    print('Seu nome é tão bonito!')
elif nome == 'Paulo' or nome == 'João' or nome == 'Pedro':
    print('Seu nome é comum no Brasil.!')
else:
    print('Seu nome é tão comum.!')
print(f'Tenha um bom dia {nome.capitalize()}!')