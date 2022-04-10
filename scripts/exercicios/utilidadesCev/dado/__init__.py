def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            return float(entrada)

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric(msg):
            valor = int(n)
            ok = True
        else:
            print(f'\033[0;031mERRO! Digite um número inteiro valido.\033[m')
        if ok:
            break
    return valor