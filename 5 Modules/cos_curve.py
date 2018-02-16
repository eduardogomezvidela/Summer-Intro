#plots cos function curve

import math
import turtle

screen=turtle.Screen()
screen.bgcolor("black")
screen.setworldcoordinates(-5,-1.1,365,1.1)
alex=turtle.Turtle()
alex.color("white")
alex.hideturtle()

x=turtle.Turtle()                           ###Plot X axis
x.speed(6)
x.color("darkblue")
x.pensize(2)
x.up()
x.goto(-8,0)
x.down()
x.goto(360,0)

y=turtle.Turtle()                           ###Plot Y axis
y.speed(6)
y.color("darkblue")
y.pensize(2)
y.left(90)
y.up()
y.goto(0,-1.1)
y.down()
y.goto(0,1.1)

for angle in range(0,360):                                              ###Plot cos curve
    spot=math.cos(math.radians(angle))                  #Note how the math.cos only accepts radians so I must invoke the math.radians() to put my degrees
    alex.goto(angle,spot)




screen.exitonclick()
