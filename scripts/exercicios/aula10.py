tempo = int(input('Quanto tempo tem o seu carro ? '))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')    
#Tambem pode se usar:
#print('Carro novo' if tempo <=3 else 'Carro velho')