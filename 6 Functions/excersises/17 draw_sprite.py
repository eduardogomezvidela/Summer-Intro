#Write a function called drawSprite that will draw a sprite.
#The function will need parameters for the turtle, the number of legs, and the length of the legs.
#Invoke the function to create a sprite with 15 legs of length 120.

import turtle
screen=turtle.Screen()
screen.bgcolor("black")
alex=turtle.Turtle()
alex.color("white")


def draw_sprite(turtle, length, legs):
    alex.pensize(25)
    alex.dot()
    alex.pensize(4)
    turtle.left(90)
    for i in range(legs):
        turtle.right(360/legs)
        turtle.forward(length)
        turtle.forward(-length)

draw_sprite(alex,120,15)

screen.exitonclick()
