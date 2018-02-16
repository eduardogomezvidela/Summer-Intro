#squares and sums

list = [5,2,4]
new_list = []
for num in range (len(list)):               #Squares all elements in list
    new_list.append(list[num]**2)

sum = 0
for num in range(len(new_list)):        #Adds together all elements in list
    sum = sum + new_list[num]

print(sum)  #Prints sum of new_list elements
    
    
