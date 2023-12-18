salario = float(input('Digite o seu salário atual: R$'))
aumento = salario + (salario*15/100)
print('O seu salário de R${:.2f}, passará a ser R${:.2f}. Isso equivale a 15% de aumento.'.format(salario, aumento))
