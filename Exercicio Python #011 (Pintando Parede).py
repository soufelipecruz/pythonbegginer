alt = float(input('Digite a altura da sua parede em metros: '))
larg = float(input('Digite a largura da sua parede em metros: '))
area = alt * larg
tinta = area / 2
print('A área da sua parede é de {:.2f}, é necessário {:.2f} litros de tinta para pinta-la.'.format(area, tinta))
