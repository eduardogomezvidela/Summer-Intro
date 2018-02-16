import turtle                                           #import turtle and prepare it for drawing
screen=turtle.Screen()
screen.bgcolor("black")
alex=turtle.Turtle()
alex.color("blue")
alex.pensize(2)

a=1
b=1       #declare "y" and "x" variables to later use in "for" loop
c=1

for i in range(14):            #No idea what this function is
    alex.forward(a)
    print(a)
    alex.left(90)
    b=a
    a=a+c
    c=b



###### This part up next is wrong ######
# It is supposed to be the actual curve of the golden ratio

a=1
b=1       #declare "y" and "x" variables to later use in "for" loop
c=1

bobby=turtle.Turtle()
bobby.color("red")
bobby.pensize(2)



for i in range(14):            #No idea what this function is
    bobby.forward(a)
    print(a)
    bobby.left(88)               #What is the correct function for this???
    b=a
    a=a+c
    c=b

a=1
b=1       #declare "y" and "x" variables to later use in "for" loop
c=1

bobby2=turtle.Turtle()
bobby2.color("yellow")
bobby2.pensize(2)



for i in range(14):            #No idea what this function is
    bobby2.forward(a)
    print(a)
    bobby2.left(86)               #What is the correct function for this???
    b=a
    a=a+c
    c=b

a=1
b=1       #declare "y" and "x" variables to later use in "for" loop
c=1

bobby3=turtle.Turtle()
bobby3.color("purple")
bobby3.pensize(2)


for i in range(14):            #No idea what this function is
    bobby3.forward(a)
    print(a)
    bobby3.left(84)               #What is the correct function for this???
    b=a
    a=a+c
    c=b

screen.exitonclick()
