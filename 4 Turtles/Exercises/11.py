#dot spiral

import turtle
screen=turtle.Screen()
screen.bgcolor("black")
alex=turtle.Turtle()
alex.color("white")
alex.up()
alex.speed(0)

alex2=turtle.Turtle()
alex2.color("hotpink")
alex2.up()
alex2.speed(0)

alex3=turtle.Turtle()
alex3.color("lightgreen")
alex3.up()
alex3.speed(0)

x=1

for i in range(150):
    alex.forward((1+x)/2)
    alex.down()
    alex.forward((1+x)/2)
    alex.up()
    alex.forward((1+x)/2)
    alex.right(15)
    alex.dot()
    alex2.forward((1+x)/2)
    alex2.down()
    alex2.forward((1+x)/2)
    alex2.up()
    alex2.forward((1+x)/2)
    alex2.right(20)
    alex2.dot()
    alex3.forward((1+x)/2)
    alex3.down()
    alex3.forward((1+x)/2)
    alex3.up()
    alex3.forward((1+x)/2)
    alex3.right(25)
    alex3.dot()
    x=x+1

screen.exitonclick()
