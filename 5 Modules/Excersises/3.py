#The Pythagorean Theorem tells us that the length of the hypotenuse of a right triangle is related to the lengths of the other two sides.
#Look through the math module and see if you can find a function that will compute this relationship for you.
#Once you find it, write a short program to try it out.

#a^2+b^2=c^2

import math

a=input("Side A:")
a=int(a)
b=input("Side B:")
b=int(b)

c=math.sqrt((a**2)+(b**2))

print("The hypotenuse of the triangle is", c)
