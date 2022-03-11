velocidade = int(input('A velocidade do carro é: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f'Você foi multado por execo de velocidade! O valo a ser pago é R$ {multa}')
print('Tenha um bom dia! Diriga com segurança!')
