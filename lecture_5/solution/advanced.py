from random import shuffle

data = [
    ('c', 't', -1),
    ('a', 'd', 5),
    ('b', 'm', 2),
    ('b', 'm', -1),
    ('b', 'm', 1),
]

list = [1,2,3,4,5]

product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num
print(product)

def a(x):
    def g(y):
        return x + y
    return g
print('result is:', a(1)(5))

aa = a(1)
print('Result from aa is: ',aa(5))


print(a and b)

# Sorting list of tuples, it happends element by element from tuple to tuple
#print(data)
#data.sort()
#print(data)

#Use dictionaries when you need fast search by key
#Use list when you need to loop into the data and need results
#for average price, or max and min price, start and end date...



