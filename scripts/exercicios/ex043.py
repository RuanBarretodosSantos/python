altura = float(input('Qual é a sua altura ? (m) '))
peso = float(input('Qual é o seu peso ? (Kg) '))
imc = peso / altura ** 2
print(f'O seu IMC é {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc == 18.5 and imc <= 24.9:
    print('Você está no peso ideal')
elif imc == 25 and imc <= 29.9:
    print('Você está com sobrepeso!')
elif imc == 30 and imc <= 40:
    print('Você está obeso!')
else:
    print('Você está com obesidade morbida!')