#keeps the turtle walking as long as it is inside the screen

import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
alex = turtle.Turtle()
alex.color("white")
alex.shape("turtle")

print(turtle.screensize())


alex.up()
alex.goto(random.randrange(-400,400),random.randrange(-400,400))
alex.down()


bobby = turtle.Turtle()
bobby.color("blue")
bobby.shape("turtle")

bobby.up()
bobby.goto(random.randrange(-400,400),random.randrange(-400,400))
bobby.down()

def r_move(turtle):
    ht = random.randrange(0,2)
    if ht == 1:
        turtle.right(random.randrange(1,91))
    else:
        turtle.left(random.randrange(1,91))
    turtle.forward(50)

def inside(window,turtle):
    #GET WINDOW COORDINATES
    width =screen.window_width()
    height=screen.window_height()

    #CHECK IF TURTLE IS WITHIN WINDOW COORDINATES
    if abs(turtle.xcor()) > (width/2) -50 or abs(turtle.ycor()) > (height/2) -50:
        turtle.right(180)
        turtle.forward(60)
        return True
    else:
        return True

#This is for when the turtles touch each other, they "bounce"
def touch(turtle1,turtle2):
    if abs(turtle1.xcor() - turtle2.xcor() < 20 and turtle1.ycor() - turtle2.ycor() < 20):
        turtle1.right(180)
        turtle1.forward(60)
        turtle2.right(180)
        turtle2.forward(60)
        return True
    else:
        return True

while (inside(screen,alex) == True and inside(screen,bobby) == True):
    touch(alex,bobby)
    r_move(alex)
    r_move(bobby)


screen.exitonclick()
