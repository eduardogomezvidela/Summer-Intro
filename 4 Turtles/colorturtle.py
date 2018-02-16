import turtle
screen = turtle.Screen()
screen.bgcolor("black")
alex=turtle.Turtle()
alex.pensize(6)

for color in ("blue", "red", "purple", "orange", "green", "yellow", "cyan", "pink"):
    alex.color(color)
    alex.forward(100)
    alex.left(45)

screen.exitonclick()
