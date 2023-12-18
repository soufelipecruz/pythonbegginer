from datetime import date
ano_nascimento = int(input('Digite o ano que você nasceu: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
menor = 18 - idade
maior = menor + idade
if idade == 18:
    print('Está na hora de se alistar!')
elif idade < 18:
    print('Ainda não é o momento, falta {} anos.'.format(menor))
else:
    print('Já deveria ter se alistado, já passou {} anos.'.format(maior))
