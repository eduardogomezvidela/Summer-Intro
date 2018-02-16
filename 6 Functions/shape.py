#Draws various shapes by defining and later calling their functions

import turtle
screen=turtle.Screen()
screen.bgcolor("black")



#Rectangle, square, triangle, octagon,  circle

def rectangle (turtle, width, length):           #Define rectangle
    turtle.color("white")
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)

def square (turtle, size):                              #Define square using the rectangle function
    turtle.color("blue")
    for i in range (4):
        turtle.forward(size)
        turtle.right(90)

def triangle (turtle, size):                                  #Define triangle
    turtle.color("yellow")
    turtle.right(60)
    for i in range(3):
        turtle.forward(size)
        turtle.right(360/3)
    turtle.right(-60)

def octagon (turtle,size):                      #Define octagon
    turtle.color("red")
    for i in range(8):
        turtle.forward(size)
        turtle.right(360/8)

def circle(turtle,size):                        #Define circle
    turtle.color("purple")
    for i in range (360):
        turtle.forward(size)
        turtle.right(1)

def main():

    alex=turtle.Turtle()
    alex.pensize(2)
    alex.speed(3)

    a=input("Rectangle width?")                         #Ask for rectangle user input
    a=int(a)
    b=input("Rectangle length?")
    b=int(b)

    rectangle(alex,a,b)                                             #Call rectangle

    a=input("Square size?")                         #Ask for square user input
    a=int(a)

    square(alex, a)                                                 #Call square

    a=input("Triangle size?")                               #Ask for triangle input
    a=int(a)

    triangle(alex,a)                                                        #Call triangle

    a=input("Octagon size?")                                #Ask for octagon input
    a=int(a)

    octagon(alex,a)                                                     #Call octagon

    a=input("Circle size? Don't make it bigger than 2")         #Ask for circle input
    a=float(a)

    circle(alex,a)                                                      #Call circle


    screen.exitonclick()

if (__name__=="__main__"):
    main()
