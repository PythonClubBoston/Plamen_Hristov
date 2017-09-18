from pprint import pprint
import random

numbers = [('person - {}'.format(n), n % 6) for n in range(10, 20)]
random.shuffle(numbers)
#pprint(numbers)

#print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# reversed_numbers = [(n[1], n[0]) for n in numbers]
# pprint(min(reversed_numbers))

print(min(numbers, key=lambda el: el[1]))

def get_second_value(el):
    return el[1]

for el in numbers:
    value = get_second_value(el)

print(min(numbers, key=get_second_value(el)))
#TODO: find the minimal value from all values returned

numbers.sort(key=lambda el: el[1])