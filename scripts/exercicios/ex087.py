matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c] 
tres = matriz[2][0] + matriz[2][1] + matriz[2][2]             
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:5}]', end='')
    print()
print(f'A soma de todos os pares dá: {par}')
print(f'A soma dos valores da terceira coluna é {tres}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')