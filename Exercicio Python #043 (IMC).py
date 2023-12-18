peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite a sua altura em metros: '))
imc = peso / (altura**2)
if imc <= 18.5:
    print('Seu IMC é de {:.1f}. Você está abaixo do peso!'.format(imc))
elif 18.5 < imc <= 25.0:
    print('Seu IMC é de {:.1f}. Você está no peso ideal!'.format(imc))
elif 25 < imc <= 30:
    print('Seu IMC é de {:.1f}. Você está com sobrepeso!'.format(imc))
elif 30 < imc <= 40:
    print('Seu IMC é de {:.1f}. Você está obeso!'.format(imc))
else:
    print('Seu IMC é de {:.1f}. Obesidade mórbida, procure um médico urgente!')
