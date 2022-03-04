velocidade = int(input('A velocidade do carro é: '))
multa = (velocidade - 80) * 7
if velocidade >=80:
    print(f'Você foi multado! O valo a ser pago é R$ {multa}')
