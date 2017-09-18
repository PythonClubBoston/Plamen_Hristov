#----------- GENERATORS

# def range_equivalent(start, end = None, step = None):
#     step = step if step is not None else 1
#     value = start
#     while end is None or value < end:
#         yield value
#         value += step
#
# gen_object = range_equivalent(1,5)
# print(gen_object)
# print(next(gen_object))
# print(next(gen_object))
# print(next(gen_object))


# for number in range_equivalent(10, 20):
#     print(number)

# with open('catalog.csv', 'r', encoding='utf-8') as f:
#     contents = f.read() #loading the whole content of the file into the memory
#
#     for line in f:
#         print(line)

import csv

