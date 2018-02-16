import turtle
screen=turtle.Screen()
screen.bgcolor("white")
alex=turtle.Turtle()
alex.color("red")
alex.pensize(3)

alex.fillcolor("blue")

alex.begin_fill()        #begins shape filling

for i in range(4):         #draws square
    alex.forward(200)
    alex.right(90)

alex.end_fill()       #finishes shape filling


screen.exitonclick()
