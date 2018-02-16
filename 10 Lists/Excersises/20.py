#odd number counter

list = [1, 3, 4, 6, 7, 8, 10, 12, 46, 23, 81, 90, 6, 43, 2] #6 odd numbers

counter = 0

for num in list:
    if num % 2 != 0:
        counter += 1

print (counter)

