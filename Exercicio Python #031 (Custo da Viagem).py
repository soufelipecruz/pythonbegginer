dist = float(input('What is the distance traveled: '))
dist_one = dist * 0.50
dist_two = dist * 0.45
if dist <= 200:
    print('The ticket price will be R${}'.format(dist_one))
else:
    print('The ticket price will be R${}'.format(dist_two))
print('Good Travel!')
