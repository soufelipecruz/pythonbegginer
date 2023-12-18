num = int(input('Digite o número da tabuada que deseja: '))
for c in range(1, 11):
    print('{}X{:2}={}'.format(num, c, num*c))
