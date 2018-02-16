#Square function

import turtle
screen=turtle.Screen()
screen.bgcolor("black")

def  draw_square(turtle,size):          #Define the function
    for i in range(1,5):
        turtle.forward(size)
        turtle.right(90)

alex=turtle.Turtle()
alex.pensize(2)
alex.color("white")

draw_square(alex,250)                   #Call the function

pete=turtle.Turtle()
pete.pensize(2)
pete.color("blue")
pete.up()
pete.backward(200)
pete.right(45)
pete.down()

draw_square(pete,130)

screen.exitonclick()



