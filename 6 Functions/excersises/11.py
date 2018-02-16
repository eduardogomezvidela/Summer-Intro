#Write a non-fruitful function drawEquitriangle(someturtle, somesize) which calls
#drawPoly from the previous question to have its turtle draw a equilateral triangle.

import turtle
import draw_poly

screen=turtle.Screen()
screen.bgcolor("black")
alex=turtle.Turtle()
alex.color("white")
alex.pensize(3)

def equi_triangle(turtle,size):
    draw_poly.draw_poly(turtle,3,size)

equi_triangle(alex,120)



screen.exitonclick()
