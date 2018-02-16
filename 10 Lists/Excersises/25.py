#Word counter up to and including 'sam'

list = ['boy', 'yay', 6, 'cheese', 1, 1, 'yay',1, 5,  'cake', 'sure', 'ok', 3, 9,6,7, 4, 'samuel', 5, 'sam', 9, 'big', 'small']

for word in list:
    if  type(word) != str:
        list.pop(list.index(word))

for word in list:
    if  type(word) != str:
        list.pop(list.index(word))
        
print(list)
print (len(list))
counter = 0

for word in list:
    if list.index(word) <list.index('sam'):
        counter +=1

print(counter+1)
