#plots log function curve after user input

import math
import turtle

screen=turtle.Screen()
screen.bgcolor("black")
screen.setworldcoordinates(-1,-1,10,10)
alex=turtle.Turtle()
alex.color("white")
alex.hideturtle()

x=turtle.Turtle()                           ###Plot X axis
x.speed(6)
x.color("darkblue")
x.pensize(2)
x.up()
x.goto(-1,0)
x.down()
x.goto(10,0)

y=turtle.Turtle()                           ###Plot Y axis
y.speed(6)
y.color("darkblue")
y.pensize(2)
y.left(90)
y.up()
y.goto(0,-1)
y.down()
y.goto(0,10)

spot=input("Insert what you wanna log")
spot=int(spot)

for angle in range(-1,10):                                              ###Plot log  curve

    if(angle==-1):                          #Makes sure that when alex moves to its place it won't draw until it is in the right place
        alex.up()
    else:
        alex.down()

    alex.goto(angle,math.log(spot))




screen.exitonclick()
