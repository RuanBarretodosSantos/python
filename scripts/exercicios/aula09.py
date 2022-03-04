from operator import invert


frase = 'Curso em Video Python'
frase2 = 'curso em video python'
frase3 = '   Aprenda Python  '
#Sem nada
print(frase)
print(frase2)
print(frase3)
#Fatiamento
print(frase[9])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[9:])
print(frase[9::2])
print(frase[::2])
#Análise
print(len(frase))
print(frase.count('e'))
print(frase.count('e', 0, 7))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)
#Transformação
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase2.title())
print(frase3.strip())
print(frase3.rstrip())
print(frase3.lstrip())
#Divisão
print(frase.split())
#Junção
print('-'.join(frase))
print(frase.split() [2] [3])