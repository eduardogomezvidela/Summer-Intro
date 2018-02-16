#clock face

import turtle
screen=turtle.Screen()
screen.bgcolor("lightgreen")
alex=turtle.Turtle()
alex.color("blue")
alex.shape("turtle")
alex.pensize(2)

alex.stamp()

for i in range(12):
    alex.up()
    alex.forward(100)
    alex.down()
    alex.forward(10)
    alex.up()
    alex.forward(15)
    alex.stamp()
    alex.forward(-125)
    alex.right(360/12)
    
    



screen.exitonclick()
