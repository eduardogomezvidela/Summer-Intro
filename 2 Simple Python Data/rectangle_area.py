#Write a program that will compute the area of a rectangle.
#Prompt the user to enter the width and height of the rectangle.
#Print a nice message with the answer.



str_width=input("How wide is the rectangle?")
str_length=input("How long is the rectangle?")

width=int(str_width)
length=int(str_length)

area= width*length
print("The rectangle is", area,"**2")
