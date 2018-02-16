#Create a list called myList with the following six items: 76, 92.3, “hello”, True, 4, 76. Do it with both append and with concatenation, one item at a time.

#APPEND

#Not efficient

list = []

list.append(76)

list.append(92.3)

list.append("hello")

list.append(True)

list.append(4)

list.append(76)

print (list)

#More efficient

words = [76,92.3,"hello",True,4,76]

list = []

for word in words:
    list.append(word)

print(list)

#CONCATENATE

#Not efficient

list = []

list = list + [76]

list = list + [92.3]

list = list + ["hello"]

list = list + [True]

list = list + [4]

list = list + [76]

print (list)

#More efficient

words = [76,92.3,"hello",True,4,76]

list = []

for word in words:
    list = list + [word]

print(list)

