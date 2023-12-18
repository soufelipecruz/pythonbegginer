radar = int(input('Velocidade: '))
multa = (radar - 80)*7
if radar > 80:
    print('Você ultrapassou o limite a via, por isso irá pagar R${}'.format(multa))
else:
    print('Tenha um bom dia e dirija com segurança!')
