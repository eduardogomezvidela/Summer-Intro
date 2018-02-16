#Write a function called drawSprite that will draw a sprite.
#The function will need parameters for the turtle, the number of legs, and the length of the legs.
#Invoke the function to create a sprite with 15 legs of length 120.

import turtle



def main():
    screen=turtle.Screen()
    screen.bgcolor("black")
    alex=turtle.Turtle()
    alex.color("white")
    draw_sprite(alex,120, 10, 5,15)
    screen.exitonclick()



def draw_sprite(turtle, length, dot,triangle, legs):
    turtle.pensize(dot)
    turtle.dot()
    for i in range(legs):
        turtle.pensize(dot)
        turtle.right(360/legs)
        turtle.forward(length)
        for i in range(3):
            turtle.pensize(triangle)
            turtle.right(120)
            turtle.forward(length/3)
        turtle.forward(-length)

if(__name__=="__main__"):
    main()


