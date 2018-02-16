"""
count
in
reverse
index
insert
"""



def count(list,item):
    counter = 0
    
    for i in list:
        if i == item:
            counter +=1
    return counter

def inside (list, item):
    for i in list:
        if i == item:
            return True
        else:
            return False

def reverse(list):                       
    new_list = []
    for i in range(len(list)-1,-1,-1):
            x = i
            new_list.append(list[x])
    return new_list

def index (list,item):
    counter = 0
    for i in list:
        if i == item:
            return counter
        else:
            counter += 1

def insert(list,location,item):
    new_list = list[:location] + [item] + list[location:]
    return new_list


list = [1,5,7,9,2,3,1]

print(count(list,1))
print(count(list,2))

print (inside(list,1))
print (inside(list,8))

print(reverse (list))

print(index(list,7))

print(insert(list, 1, 'yes'))
print(insert(list, 4, 'ok'))
