from random import choice
one = str(input('Digite o nome do seu primeiro aluno: '))
two = str(input('Digite o nome do seu segundo aluno: '))
tree = str(input('Digite o nome do seu terceiro aluno: '))
four = str(input('Digite o nome do seu quarto aluno: '))
alunoaleatorio = choice([one, two, tree, four])
print('O aluno escolhido de forma aleatória foi {}'.format(alunoaleatorio))
