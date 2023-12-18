import math
ang = float(input('Digite o valor do ângulo: '))
sen = math.sin(math.radians(ang))
cose = math.cos(math.radians(ang))
tan = math.atan(math.radians(ang))
print('O seno do ângulo {} é {:.3f}, o cosseno é {:.3f} e a tangente é {:.3f}.'.format(ang, sen, cose, tan))
