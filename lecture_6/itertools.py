# https://docs.python.org/3/library/itertools.html - DOCUMENTAION

import itertools

elements = [n for n in range(1, 6)]

# print(list(itertools.combinations(elements, 2)))
# print(list(itertools.permutations(elements, 2)))

numbers = [n for n in range(1,6)]
letters = [n for n in 'ABCDE']

print(list(itertools.product(numbers, letters)))

# dir(itertools)
# help(itertools.combinations)
# help(itertools.permutations)
help(itertools.product)