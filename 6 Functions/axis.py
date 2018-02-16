#draws an x y axis

import turtle


def axis(llx,lly,urx,ury):
    
    x=turtle.Turtle()                           ###Plot X axis
    x.speed(6)
    x.color("darkblue")
    x.pensize(2)
    x.hideturtle()
    x.up()
    x.goto(llx,0)
    x.down()
    x.goto(urx,0)
    x.stamp()
    x.up()
    x.goto(urx-0.4,-0.5)
    x.write("x",font=("Arial", 12, "normal"))

    y=turtle.Turtle()                           ###Plot Y axis
    y.speed(6)
    y.color("darkblue")
    y.pensize(2)
    y.hideturtle()
    y.left(90)
    y.up()
    y.goto(0,lly)
    y.down()
    y.goto(0,ury)
    y.stamp()
    y.up()
    y.goto(-0.3,ury-0.7)
    y.write("y", font=("Arial", 12, "normal"))

def main():
    screen=turtle.Screen()
    screen.bgcolor("black")
    screen.setworldcoordinates(-11,-11,11,11)
    axis(-10,-10,10,10)

    
    screen.exitonclick()


if (__name__=="__main__"):
    main()
    
