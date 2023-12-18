salario = float(input('Digite o seu salário: '))
sal_sup = (salario/10) + salario
sal_inf = (salario * 15/100) + salario
if salario > 1.250:
    print('Quem ganha R${}, passará a ganhar R${}.'.format(salario, sal_sup))
else:
    print('Quem ganha R${}, passará a ganhar R${}.'.format(salario, sal_inf))
