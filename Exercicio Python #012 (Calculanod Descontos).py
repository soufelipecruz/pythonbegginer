preco = float(input('Digite o preço do produto: R$'))
desconto = preco - (preco * 5/100)
print('O preço aplicando 5% de desconto ficará R${:.2f}'.format(desconto))
