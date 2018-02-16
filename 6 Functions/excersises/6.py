#Use the drawsquare function we wrote in this chapter in a program to draw the image shown below.
#Assume each side is 20 units. (Hint: notice that the turtle has already moved away from the ending point of the last square when the program ends.)

#5 squares size 20

import turtle
import draw_square

screen=turtle.Screen()
screen.bgcolor("lightgreen")

alex=turtle.Turtle()
alex.color("hotpink")
alex.pensize(3)
alex.speed(5)

for i in range(5):
    draw_square.draw_square(alex,20)
    alex.up()
    alex.forward(40)
    alex.down()

























screen.exitonclick()
