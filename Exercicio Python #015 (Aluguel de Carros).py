km = float(input('Digite a quantidade de Km foram percorridos: '))
dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))
preco = (dias * 60) + (0.15 * km)
print('O valor a pagar pelos {} dias e {:.2f}km rodados é de R${:.2f}'.format(dias, km, preco))
