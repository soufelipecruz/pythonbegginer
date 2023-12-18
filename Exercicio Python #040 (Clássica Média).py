media_one = float(input('Digite sua primeira nota: '))
media_two = float(input('Digite sua segunda nota: '))
media = (media_one + media_two)/2
if media < 5.0:
    print('Sua média foi {:.2f}. Você está reprovado.'.format(media))
elif 5.0 <= media < 6.9:
    print('Sua média foi {:.2f}. Você esta em recuperação.'.format(media))
elif media > 7:
    print('Sua média foi {:.2f}. Parabéns, você foi aprovado!'.format(media))
