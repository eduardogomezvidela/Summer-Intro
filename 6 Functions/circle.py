#Draw circle with a function

import turtle


def draw_circle(turtle,size):
    for i in range(0,360):
        turtle.forward(size)
        turtle.right(1)



def main():
    screen=turtle.Screen()
    screen.bgcolor("black")
    alex=turtle.Turtle()
    alex.color("hotpink")
    alex.pensize(2)
    alex.speed(0)

    draw_circle(alex,3)
    draw_circle(alex,2)

    screen.exitonclick()

if ( __name__ == "__main__"):
    main()
