r1 = float(input('Primeiro: '))
r2 = float(input('Segundo: '))
r3 = float(input('Terceiro: '))
equi = r1 == r2 == r3
isos = r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2
esca = r1 != r2 != r3
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and equi:
    print('Os segmentos acima podem formar um triângulo {}!'.format('equilátero'))
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and isos:
    print('Os segmentos acima podem formar um triângulo {}!'.format('isósceles'))
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and esca:
    print('Os segmentos acima podem formar um triângulo {}!'.format('escaleno'))
else:
    print('Os segmentos acima NÃO podem formar um triângulo!')
