def teste(b):
    global a
    a = 8
    print(f'A dentro vale {a}')


a = 5
teste(a)
print(f'A fora vale {a}')    