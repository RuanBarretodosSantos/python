from re import S


n1 = int(input('Um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A sua soma é {}, o produto é {}, \n divisão é {:.4f},'.format(s, m, d), end='')
print(' divisão inteira {:.3f} e pôtencia {}.'.format(di, e))