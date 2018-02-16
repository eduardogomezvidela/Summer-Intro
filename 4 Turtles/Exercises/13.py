#A sprite is a simple spider shaped thing with n legs coming out from a center point. The angle between each leg is 360 / n degrees.
#Write a program to draw a sprite where the number of legs is provided by the user.

import turtle
screen=turtle.Screen()
screen.bgcolor("black")
alex=turtle.Turtle()
alex.color("white")

alex.pensize(15)
alex.dot()
alex.pensize(2)

legs=input("How many legs?")
legs=int(legs)

for i in range(legs):
    alex.forward(100)
    alex.forward(-100)
    alex.right(360/legs)

screen.exitonclick()
