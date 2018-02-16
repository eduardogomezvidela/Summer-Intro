import turtle
screen=turtle.Screen()
screen.bgcolor("hotpink")

alex=turtle.Turtle()
alex.shape("square")

alex.penup()
x=1

for i in range (1000):
    alex.stamp()
    alex.right(20)
    x=x+0.5
    alex.forward(x)






screen.exitonclick()
