data = [
    ('c', 't', -1),
    ('a', 'd', 5),
    ('b', 'm', 2),
    ('b', 'm', -1),
    ('b', 'm', 1),
]


# Sorting list of tuples, it happends element by element from tuple to tuple
print(data)
data.sort()
print(data)

#Use dictionaries when you need fast search by key
#Use list when you need to loop into the data and need results
#for average price, or max and min price, start and end date...