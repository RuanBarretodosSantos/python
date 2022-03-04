from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print(f'O ângulo de {ang} tem o SENO de {seno:.2f} \n O ângulo de {ang} tem o COSSENO de {cosseno:.2f} \n O ângulo de {ang} tem a TANGENTE de {tangente:.2f}')