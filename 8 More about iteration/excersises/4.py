#keeps the turtle walking as long as it is inside the screen

import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
alex = turtle.Turtle()
alex.color("white")
alex.shape("turtle")

def inside(window,turtle):
    #GET WINDOW COORDINATES
    width =screen.window_width()
    height=screen.window_height()

    #CHECK IF TURTLE IS WITHIN WINDOW COORDINATES
    if abs(turtle.xcor()) > width/2 or abs(turtle.ycor()) > height/2:
        print("Turtle has escaped!")
        return False
    else:
        return True

while(inside(screen,alex) == True):
    ht = random.randrange(0,2)
    if ht == 1:
        alex.right(random.randrange(1,91))
    else:
        alex.left(random.randrange(1,91))
    alex.forward(20)


screen.exitonclick()
