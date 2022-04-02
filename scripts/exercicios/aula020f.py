def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
        

lista = [3, 8, 5, 7, 1]
dobra(lista)
print(lista)