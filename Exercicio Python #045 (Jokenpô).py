from random import randint
from time import sleep
for c in range(0, 3):
    print('++++++ VAMOS JOGAR JOKENPÔ? ++++++')
    print(''''Escolha uma das opções abaixo:
    [1] Pedra
    [2] Papel
    [3] Tesoura''')
    opcao = int(input('Digite a opção desejada: '))
    opcao_comp = randint(1, 3)
    print('Jo')
    sleep(0.5)
    print('ken')
    sleep(0.5)
    print('pô!!!')
    sleep(0.5)
    print('Eu escolhi a opção {}.'.format(opcao_comp))
    result_one = opcao == 1 == opcao_comp or opcao == 2 == opcao_comp or opcao == 3 == opcao_comp
    result_two = opcao == 1 and opcao_comp == 2
    result_three = opcao == 2 and opcao_comp == 1
    result_four = opcao == 1 and opcao_comp == 3
    result_five = opcao == 3 and opcao_comp == 1
    result_six = opcao == 2 and opcao_comp == 3
    result_seven = opcao == 3 and opcao_comp == 2
    if result_one:
        print('EMPATE!')
    elif result_two:
        print('Você venceu!')
    elif result_three:
        print('Você perdeu!')
    elif result_four:
        print('Você venceu!')
    elif result_five:
        print('Você venceu!')
    elif result_six:
        print('Você perdeu!')
    elif result_seven:
        print('Você venceu!')
