import turtle
screen=turtle.Screen()
screen.bgcolor("black")
alex=turtle.Turtle()
alex.color("white")
alex.pensize(3)
alex.speed(0)

def main():
    
    draw_star(alex,300,15)
    screen.exitonclick()

def draw_star(turtle,size, points):
    for i in range(points):
        turtle.forward(size)
        turtle.right(180-180/points)

if (__name__=="__main__"):
    main()


