print('==' * 10)
print('Conversor de Base númerica.')
num = int(input('Digite um número inteiro que deseja converter: '))
base = int(input('Digite 1 para binário, 2 para octal e 3 para hexadecimal: '))
if base == 1:
    print('{} convertido para binário é {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} convertido para octal é {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente!')
