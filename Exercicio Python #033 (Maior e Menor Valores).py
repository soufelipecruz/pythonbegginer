num_one = int(input('Digite o primeiro valor: '))
num_two = int(input('Digite o segundo valor: '))
num_three = int(input('Digite o terceiro valor: '))
menor = num_one
if num_two < num_one and num_two < num_three:
    menor = num_two
if num_three < num_one and num_three < num_two:
    menor = num_three
maior = num_one
if num_two > num_one and num_two > num_three:
    maior = num_two
if num_three > num_one and num_three > num_two:
    maior = num_three
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))
