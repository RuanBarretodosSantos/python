print('Esse são todos os números pares que estão no intervalo entre 1 e 50:')
enfeite = '-=' * 7
print(f'{enfeite} PARES DE 1 ATÉ 50 {enfeite}')
for c in range(2, 51, 2):
    print(c, end=' ')
print('Acabou...')