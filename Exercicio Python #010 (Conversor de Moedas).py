cart = float(input('Digite o valor que você tem disponível em reais: '))
conv = float(cart / 4.99)
print('Com o valor de R${:.2f}, você pode por comprar U${:.2f}'.format(cart, conv))