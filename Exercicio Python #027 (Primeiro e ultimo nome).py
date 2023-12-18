name = str(input('Write your full name: ')).strip()
div = name.split()
print('Nice to meet you!')
print('Your first name is {}.'.format(div[0]))
print('Your last name is {}.'.format(div[len(div)-1]))

