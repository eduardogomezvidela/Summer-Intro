import turtle
screen=turtle.Screen()
screen.bgcolor("black")
alex=turtle.Turtle()
alex.color("orange")
alex.pensize(2)
alex.speed(0)

x=0

for i in range (83):
    alex.right(90)
    alex.forward(x+4)
    x=x+4

screen.exitonclick()
