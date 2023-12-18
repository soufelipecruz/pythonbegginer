r1 = float(input('Primeiro: '))
r2 = float(input('Segundo: '))
r3 = float(input('Terceiro: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima NÃO podem formar um triângulo!')

print('\033[4;30;45mOlá, Mundo!\033[m')