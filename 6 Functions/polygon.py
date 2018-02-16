#Draws a polygon with the function draw_poly

import turtle
screen=turtle.Screen()
screen.bgcolor("black")
alex=turtle.Turtle()
alex.color("white")
alex.pensize(2)

def draw_poly (turtle,sides,length):
    for i in range(0,sides):
        turtle.forward(length)
        turtle.right(360/sides)

draw_poly(alex,6,90)

alex.color("red")

one=input("Sides:")
one=int(one)
two=input("Length of each side:")
two=int(two)

draw_poly(alex,one,two)





screen.exitonclick()
