num = int(input('Digite um número para ver sua tabuada: '))
enfeite = '-=' * 7
print(f'{enfeite} TABUADA DE {num} {enfeite}')
for tabuada in range(0, 11):
    print(f'{num} X {tabuada:2} = {num * tabuada}')
print(f'{enfeite} F I M {enfeite}')