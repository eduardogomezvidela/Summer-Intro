import turtle
screen=turtle.Screen()
screen.bgcolor("white")

alex=turtle.Turtle()
alex.color("white")
alex.forward(470)
alex.right(90)
alex.forward(300)

#paint bottom blue strip
alex.pensize(320)
alex.color("cyan")
alex.right(90)
alex.forward(950)

alex2=turtle.Turtle()
alex2.color("white")
alex2.forward(470)
alex2.left(90)
alex2.forward(300)

#paint bottom blue strip
alex2.pensize(320)
alex2.color("cyan")
alex2.left(90)
alex2.forward(950)

sun=turtle.Turtle()
sun.color("yellow")
sun.pensize(250)
sun.forward(0.1)

screen.exitonclick()
