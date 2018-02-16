#Excersise 8

import turtle
screen=turtle.Screen()
screen.bgcolor("lightgreen")
alex=turtle.Turtle()
alex.color("hotpink")
alex.pensize(3)

import draw_poly

draw_poly.draw_poly(alex,8,40)




screen.exitonclick()
