import math
import turtle

wn = turtle.Screen()
wn.setworldcoordinates(-5,-1.25,365,1.25)
wn.bgcolor('lightblue')

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

fred = turtle.Turtle()
fred.hideturtle()
#your code here
for angle in range(0,360):
    spot=math.sin(math.radians(angle))
    fred.goto(angle,spot)
    #print(spot*10)

wn.exitonclick()
