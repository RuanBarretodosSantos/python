while True:
    num = int(input('Quer ver a tabuada de qual valor ? '))
    print('-----' * 7)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} X {c} = {num * c}')
    print('-----' * 7)
print('PROGAMA DE TABUADA EMCERRADO. Volte sempre.')