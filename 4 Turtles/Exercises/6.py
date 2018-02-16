#Write a program that asks the user for the number of sides, the length of the side, the color, and the fill color of a regular polygon.
#The program should draw the polygon and then fill it in.

import turtle
screen=turtle.Screen()
screen.bgcolor("white")
alex=turtle.Turtle()
alex.pensize(3)

sides=input("How many sides?")
length=input("How long are the sides?")
color=input("What color is the border?")
fillcolor=input("What color is the fill in?")

sides=int(sides)
length=int(length)

alex.color(color)
alex.fillcolor(fillcolor)

alex.begin_fill()
for i in range(sides):
    alex.forward(length)
    alex.right(360/sides)
alex.end_fill()

screen.exitonclick()
