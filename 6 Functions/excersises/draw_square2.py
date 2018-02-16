#This function will draw 4 squares inside a square

import turtle

def square (turtle,size):
    for i in range (4):
        turtle.forward(size)
        turtle.right(90)

def draw_square(turtle,size):
    for i in range(4):
        square(turtle,size/4)
        turtle.right(90)

def main():
    screen=turtle.Screen()
    screen.bgcolor("black")
    alex=turtle.Turtle()
    alex.color("orange")
    draw_square(alex,60)
    screen.exitonclick()


if (__name__=="__main__"):
    main()
