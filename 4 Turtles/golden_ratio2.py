import turtle                                           #import turtle and prepare it for drawing
screen=turtle.Screen()
screen.bgcolor("black")
alex=turtle.Turtle()
alex.color("blue")
alex.pensize(2)

a=1
b=1       #declare "y" and "x" variables to later use in "for" loop
c=1
d=1.618

for i in range(10):            #No idea what this function is
    alex.forward(1+d)
    print(a)
    alex.left(90)
    b=a
    a=a+c
    c=b
    d=d+d

a=1
b=1       #declare "y" and "x" variables to later use in "for" loop
c=1
d=1.618

alex2=turtle.Turtle()
alex2.color("red")
alex2.pensize(2)

for i in range(10):            #No idea what this function is
    alex2.forward((1+d)*2)
    print(a)
    alex2.left(90/2)
    b=a
    a=a+c
    c=b
    d=d+d

###### This part up next is wrong ######
# It is supposed to be the actual curve of the golden ratio

a=1
b=1       #declare "y" and "x" variables to later use in "for" loop
c=1

bobby=turtle.Turtle()
bobby.color("red")
bobby.pensize(2)


screen.exitonclick()
