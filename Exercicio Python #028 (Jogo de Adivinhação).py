from random import randint
from time import sleep
print('===' *18)
n_usuario = int(input('Adivinhe qual o número que estou pensando: '))
print('Processando...')
sleep(3)
n_comp = randint(0, 5)
if n_usuario == n_comp:
    print('PARABÉNS!!! É exatamente o número que eu estava pensando!')
else:
    print('Ganhei! Você errou!')
