import turtle
screen=turtle.Screen()
screen.bgcolor("black")
alex=turtle.Turtle()
alex.color("white")
alex.hideturtle()
alex.pensize(3)

def main():
    
    draw_star(alex,300)
    screen.exitonclick()

def draw_star(turtle,size):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

if (__name__=="__main__"):
    main()


