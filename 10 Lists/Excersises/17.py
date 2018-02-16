"""
Create a list containing 100 random integers between 0 and 1000 (use iteration, append, and the random module).
Write a function called average that will take the list as a parameter and return the average.
"""

import random

def average(list):
    length = (len(list))
    total = 0
    for num in list:
        total = total + num
    answer = total / length
    return answer



list = ([])

for i in range (100):                                   #Create a list with 100 random ints from 0-1000
    x = random.randrange(0,1001)
    list.append(x)

print(list)

print(*list)


print("Average: " ,average(list))
