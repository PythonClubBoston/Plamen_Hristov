name = input('You first and last name with space, pls')
if (len(name) == 0):
    name = input('First Name and Last Name, pls!!! ')
initials = ''

n2 = name.split(' ')
for name in n2:
    initials += name[0] + '.'
print(initials)