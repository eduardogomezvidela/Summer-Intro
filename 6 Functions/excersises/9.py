import turtle
screen=turtle.Screen()
screen.bgcolor("black")
alex=turtle.Turtle()
alex.color("orange")
alex.pensize(3)
alex.speed(0)

import draw_square2

for i in range (5):
    draw_square2.draw_square(alex,300)
    alex.right(360/20)


screen.exitonclick()
