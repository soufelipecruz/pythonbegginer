v_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do salário: R$'))
temp_pag = int(input('Em quantos anos pretende pagar: '))
prest_mensal = v_casa/(temp_pag * 12)
porcent = (salario*30)/100
if prest_mensal <= porcent:
    print('Para pagar uma casa de R${} em {} anos, a prestação será de R${:.2f}.'.format(v_casa, temp_pag, prest_mensal))
    print('Parabéns, o seu empréstimo foi APROVADO!')
elif prest_mensal > porcent:
    print('Para pagar uma casa de R${} em {} anos, a prestação será de R${:.2f}.'.format(v_casa, temp_pag, prest_mensal))
    print('Infelizmente seu empréstimo foi NEGADO.')
