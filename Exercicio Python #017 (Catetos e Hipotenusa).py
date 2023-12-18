from math import hypot
cato = float(input('Digite o comprimento do cateto oposto: '))
cata = float(input('Digite o comprimento do cateto adjacente: '))
hip = hypot(cato, cata)
print('Fazendo o calculo usando os valores do CO e do CA, o valor da hipotenusa é {:.2f}'.format(hip))
