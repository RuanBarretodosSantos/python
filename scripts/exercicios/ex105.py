def notas(*a, sit = False):
    """
    A: Desapacotar os números
    sit: Opcional da situção
    """
    dados = {}
    total = 0
    soma = 0
    for c in a:
        total += 1
        soma += c
    dados['total'] = total
    dados['maior'] = max(a)
    dados['menor'] = min(a)
    dados['média'] = soma / total
    if sit == True:
        if dados['média'] > 7:
            dados['situação'] = 'APROVADO'
        elif dados['média'] >= 5 and dados['média'] < 7:
            dados['situação'] = 'RAZOÁVEL' 
        elif dados['média'] < 5:
            dados['situação'] = 'REPROVADO'   
    return dados


# Progama principal                                   
resp = notas(5.5, 1, 0, 6.5, sit = True)    
print(resp)
