#using a Monte Carlo method simulation to calculate Pi

import turtle
import math
import random
import circle

fred = turtle.Turtle()
fred.speed(0)
screen = turtle.Screen()
screen.setworldcoordinates(-1,-1,1,1)
alex = turtle.Turtle()
alex.speed(0)
turtle.tracer(1000)

alex.hideturtle()
alex.up()
alex.goto(0,1)
alex.forward(-0.009)
alex.down()
circle.draw_circle(alex,0.0174)                 #This circle is not completely accurate but it is for the most part

fred.up()

numdarts = 5000
count=0

for i in range(numdarts):                                                       #Makes the random dots
    randx = random.randrange(-1000,1000)
    randx = randx/1000
    randy = random.randrange(-1000,1000)
    randy = randy/1000

    x = randx
    y = randy
    
    print(x)
    print(y)


    
    fred.goto(x,y)

    if (fred.distance(0,0) > 1):
        fred.color("blue")
    else:
        fred.color("red")
        count = count+1

    fred.dot()

print("There are", count, "dots inside the circle")

pi = (count/numdarts)*4

print(pi)


screen.exitonclick()
