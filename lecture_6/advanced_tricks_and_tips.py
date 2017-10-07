#----------- DEFAULT VALUES

# def display_list(l: list=None):
#     for element in l or []:
#         print(element)
#
# #display_list([1,2,3])
#
# display_list(None)

#-----------LIST COMPREHENSIONS


# squares = []
#
# for n in range(10):
#     squares.append(n**2)
#
# print(squares)

#above code is the same like the one below

# squares2 = [n**2 for n in range(10)]
# print(squares2)
#
# s = 'Създаване на филтриран списък от нещо'
#
# chars = [ch.upper() for ch in s]
#
# print(chars)

#-----------SET COMPREHENSIONS

# s = 'Създаване на филтриран списък от нещо'
#
# print(set(s))
#
# unique_letters = {ch.lower() for ch in s}
# print(unique_letters)

#-----------DICT COMPREHENSIONS

# numbers_to_squares = {}
#
# print({ n: n**2 for n in range(10)})

#----------- COMPREHENSIONS

# even_numbers_to_squares = {n**2 for n in range(10) if n % 2 == 0 }
# print(even_numbers_to_squares)
#
# even_numbers_to_squares1 = [ n**2 for n in range(10) if n % 2 == 0 ]
# print(even_numbers_to_squares1)

#----------- UNPACKING

# x, y = 200, 100
# print('{}, {}'.format(x, y))
#
# data = (100, 110)
# x1, y1 = data
# print('{}, {}'.format(x1, y1))
#
# data1 = [10, 20, 30, 40]
#
# x2, y2, *rest = data1
#
# print(x2)
# print(y2)
# print(rest)


numbers = [1, 2, 3, 4, 5]

sum_numbers = max(numbers)

print(sum_numbers)

