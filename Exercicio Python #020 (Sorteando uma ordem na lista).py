import random
one = str(input('Digite o nome do seu primeiro aluno: '))
two = str(input('Digite o nome do seu segundo aluno: '))
three = str(input('Digite o nome do seu terceiro aluno: '))
four = str(input('Digite o nome do seu quarto aluno: '))
lista = [one, two, three, four]
random.shuffle(lista)
print('O aluno escolhido de forma aleatória foi: ')
print(lista)
