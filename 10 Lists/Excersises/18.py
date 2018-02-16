"""
Write a Python function that will take a the list of 100 random integers between 0 and 1000 and return the maximum value.
(Note: there is a builtin function named max but pretend you cannot use it.)
"""

import random


list = ([])

for i in range (100):                                   #Create a list with 100 random ints from 0-1000
    x = random.randrange(0,1001)
    list.append(x)

print(list)

list.sort()

print('\n', list)

print('\n', list[-1])
