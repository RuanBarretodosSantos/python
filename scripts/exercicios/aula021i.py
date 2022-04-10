def par(a=0):
    if a % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
print(par(num))