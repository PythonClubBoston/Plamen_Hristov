#https://pymotw.com/2/itertools/

from itertools import *

#Merging and Splitting Iterators

# The chain()

# function takes several iterators as arguments and returns
# a single iterator that produces the contents of
# all of them as though they came from a single sequence.


#
# for i in chain([1, 2, 3], ['a', 'b', 'c']):
#     print(i)

# izip()

# returns an iterator that combines the elements of
# several iterators into tuples. It works like the built-in function zip(),
# except that it returns an iterator instead of a list.

from itertools import *

# for i in zip([1, 2, 3], ['a', 'b', 'c']):
#     print (i)

#  The islice()

# function returns an iterator which returns selected items
#  from the input iterator, by index. It takes the same arguments as the
#  slice operator for lists: start, stop, and step. The start and step
#  arguments are optional.

# print ('Stop at 5:')
# for i in islice(count(),5):
#     print (i)

# The tee()

# function returns several independent iterators (defaults to 2)
# based on a single original input. It has semantics similar to the Unix
# tee utility, which repeats the values it reads from its input and writes
# them to a named file and standard output.

# r = islice(count(),1, 3)
# print(type(r))
# i1, i2 = tee(r)
#
# for i in i1:
#     print('i1: ', i*2)
#
# for i in i2:
#     print('i2: ', i*2)

# Converting Inputs

# The imap()
#
# function returns an iterator that calls a function on the values
#  in the input iterators, and returns the results.
# It works like the built-in map(), except that it stops when any input
# iterator is exhausted (instead of inserting None values to completely
# consume all of the inputs).
#
# In the first example, the lambda function multiplies the input values by 2. In a second example, the lambda function multiplies 2 arguments, taken from separate iterators, and returns a tuple with the original arguments and the computed value.
from itertools import *

# help(range)
# print('Doubles: ')
#
# for i in map(lambda x: x*2, range(5)):
#     print(i)

# for i in map(lambda x, y:(x, y, x*2), range(5), range(5,10)):
#     print('%d * %d = %d' % i)

#  The starmap()

#  function is similar to imap(), but instead of constructing
#  a tuple from multiple iterators it splits up the items in a single
#  iterator as arguments to the mapping function using the * syntax.
#  Where the mapping function to imap() is called f(i1, i2), the mapping
#  function to starmap() is called f(*i).

# print('Multiples')
#
# values = [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
#
# for i in starmap(lambda x, y: (x, y, x*y), values):
#     print('%d * %d = %d' % i)

# Producing New Values

# The count()
#
#  function returns an interator that produces consecutive
# integers, indefinitely. The first number can be passed as an argument,
# the default is zero. There is no upper bound argument
# (see the built-in xrange() for more control over the result set).
# In this example, the iteration stops because the list argument is
# consumed.

# for i in zip(count(1,2), ['a', 'b', 'c']):
#     print(i)

# The cycle()
#
# function returns an iterator that repeats the contents of
# the arguments it is given indefinitely. Since it has to remember the
# entire contents of the input iterator, it may consume quite a bit of
# memory if the iterator is long. In this example, a counter variable is
# used to break out of the loop after a few cycles.

# i = 0

# for item in cycle(['a', 'b', 'c']):
#     i += 1
#     if i == 10:
#         break
#     print('({}, {})'.format(i, item))

# The repeat()
#
# function returns an iterator that produces the same value
# each time it is accessed. It keeps going forever, unless the optional
# times argument is provided to limit it.

# from itertools import *
#
# for i in repeat('over-and-over', 5):
#     print (i)

# It is useful to combine repeat() with izip() or imap() when invariant
#  values need to be included with the values from the other iterators.

# for i, s in zip(count(), repeat('over-and-over', 5)):
#     print(i, s)



# for i in map(lambda x,y:(x, y, x*y), repeat(2), range(5)):
#     print ('%d * %d = %d' % i)

#Filtering

# The dropwhile()
#
# function returns an iterator that returns elements
#  of the input iterator after a condition becomes false for the first
#  time. It does not filter every item of the input; after the condition
#  is false the first time, all of the remaining items in the input are
#  returned.

# import itertools
#
#
# def should_drop(x):
#     print('Testing:', x)
#     return(x<1)
#
# for i in itertools.dropwhile(should_drop, [ -1, 0, 1, 2, 3, 4, 1, -2 ]):
#     print('Yielding:', i)

# The opposite of dropwhile(), takewhile() returns an iterator that
# returns items from the input iterator as long as the test function
# returns true.

# from itertools import *
#
# test_results = []
# def should_take(x):
#     print('Testing:', x)
#     test_results.append(x)
#     return (x<2)
#
# yield_results = []
# for i in takewhile(should_take, [ -1, 0, 1, 2, 3, 4, 1, -2 ]):
#     print('Yielding:', i)
#     yield_results.append(i)
#
# print(yield_results)
# print(test_results)

#ifilter()

# returns an iterator that works like the built-in filter()
#  does for lists, including only items for which the test function
# returns true. It is different from dropwhile() in that every item
#  is tested before it is returned.

# from itertools import *
#
# def check_item(x):
#     print('Testing:', x)
#     return (x<1)
#
# for i in filter(check_item, [ -1, 0, 1, 2, 3, 4, 1, -2 ]):
#     print('Yielding:', i)


# Grouping Data

# The groupby()
#
# function returns an iterator that produces sets of values
# grouped by a common key.
#
# This example from the standard library documentation shows how to group
# keys in a dictionary which have the same value:







