import turtle
screen=turtle.Screen()
screen.bgcolor("black")
alex=turtle.Turtle()
alex.color("white")
alex.hideturtle()
alex.pensize(3)

def draw_star(size):
    for i in range(5):
        alex.forward(size)
        alex.right(144)

draw_star(300)




screen.exitonclick()
