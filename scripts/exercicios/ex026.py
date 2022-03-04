from posixpath import split


frase = str(input('Escreva uma frase: ')).strip().lower()
contador = frase.count('a')
achar = frase.find('a') + 1
achar2 = frase.rfind('a') + 1
print(f'A letra "A" aparece {contador} vezes na frase. A primeira vez foi na posição {achar}, a ultima foi no {achar2}' )