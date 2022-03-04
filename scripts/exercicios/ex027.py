nome = str(input('Qual é seu nome ? ')).strip()
n = nome.split()
n2 = n[len(n) - 1]
print('Seu primeiro nome é', n[0])
print(f'Seu ultimo nome é {n2}')