def teste(b):
    a = 8 #A LOCAL
    b += 4
    c = 2
    print(f'A dentro vale {a}') 
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5 #A GLOBAL    
teste(a)
print(f'A fora vale {a}')