#Let's user draw with the turtle by clicking

import turtle
screen=turtle.Screen()
screen.bgcolor("white")
alex=turtle.Turtle()
alex.color("black")

alex.shape(turtle)

screen.onscreenclick(alex.goto)




