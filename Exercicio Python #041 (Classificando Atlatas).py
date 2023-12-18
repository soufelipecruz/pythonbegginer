from datetime import date
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print('Sua idade é de {}'.format(idade))
if idade <= 9:
    print('Atleta Mirim!')
elif 9 < idade <= 14:
    print('Atleta Infantil!')
elif 14 < idade <= 19:
    print('Atleta Júnior!')
elif 19 < idade <= 25:
    print('Atleta Sênior!')
elif idade > 25:
    print('Atleta Master!')
