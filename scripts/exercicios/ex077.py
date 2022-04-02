lista = ('APRENDER', 'PROGAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGAMADOR', 'FUTURO')
for r in lista:
    print(f'\nNa palavra {r} temos ', end=' ')
    for letra in r:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')