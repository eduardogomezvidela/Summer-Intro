import turtle
screen=turtle.Screen()
screen.bgcolor("black")
alex=turtle.Turtle()
alex.color("orange")
alex.pensize(2)
alex.speed(0)

x=0
y=90

for i in range (103):
    alex.right(y)
    alex.forward(x+4)
    x=x+4
    y=y-0.02

screen.exitonclick()
