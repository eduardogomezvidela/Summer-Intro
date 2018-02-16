#adder up to first even number

list = [1, 35, 7, 5, 11, 6, 7, 3, 4, 6, 8, 10, 11] #1 + 35 + 7 + 5 + 11 == 59

adder = 0

new_list = []

for num in list:
    new_list.append(num%2)

up_to = (new_list.index(0))             #Gets up to what number we will add (even number)


counter = 0
answer = 0

for num in list:                                    #Adds numbers up to even number
    if counter < up_to:
        answer = answer+num
        counter += 1

print(answer)
