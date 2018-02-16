#function that can draw polygons



def draw_poly(turtle,sides,size):
    for i in range (sides):
        turtle.forward(size)
        turtle.left(360/sides)

def main():
    import turtle
    screen=turtle.Screen()
    screen.bgcolor("black")
    alex=turtle.Turtle()
    alex.color("white")

    draw_poly(alex,8,20)

    screen.exitonclick()


if (__name__=="__main__"):
    main()

