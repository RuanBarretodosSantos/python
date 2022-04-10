from datetime import date


def voto(a=0):
    b = date.today().year - a
    if b >= 18:
        return f'Com {b} anos: VOTO OBRIGTÓRIO'
    elif b < 18:
        if b >= 16:
            return f'Com {b} anos: VOTO OPCIONAL'
        else:
            return f'Com {b} anos: VOTO NEGADO!'

    
print('-' * 30)
ano = int(input('Em que ano você nasceu ? '))    
print(voto(ano))