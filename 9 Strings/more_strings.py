colors = "red,yellow,green"

print(colors[0:3]) #Prints red

y = (colors[4:10]) #Prints yellow
print(y)

print(colors[:5])

print(colors[5:])

print(len(colors))

print(colors[len(colors)-1])    #Prints last letter in string

print(colors[:]) #Will print everything

print(ord("a"))
print(ord("A"))

print("------------------------------------------------")

a = "zero"

if a < "zebra":
    print("Your word", a, "comes before zebra")
elif a > "zebra":
    print("Your word " + a + " comes after zebra")
else:
    print("Your word is zebra")

a = "apple"

if a < "zebra":
    print("Your word", a, "comes before zebra")
elif a > "zebra":
    print("Your word " + a + " comes after zebra")
else:
    print("Your word is zebra")

print("------------------------------------------------")

print ("apple" > "Apple")

print ("zebra" < "apple")

print("------------------------------------------------")

b ="ball"

h="h"+(b[1:])

print(h)

print("------------------------------------------------")

for x in "Hello world!":
    print(x)

hello = "Hello world"
for y in range( len(hello)-1,-1,-1):
    print (hello[y])
