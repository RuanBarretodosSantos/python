from email.utils import collapse_rfc2231_value


metros = int(input('Digite quantos metros são: '))
cal1 = metros / 1000
cal2 = metros / 100
cal3 = metros / 10
cal4 = metros * 10
cal5 = metros * 100
cal6 = metros * 1000
print(f'A medida de {metros} corresponde a \n {cal1}km \n {cal2}hm \n {cal3}dam \n {cal4}dm \n {cal5}cm \n {cal6}mm')