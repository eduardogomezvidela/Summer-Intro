import shape
import turtle

screen=turtle.Screen()
alex=turtle.Turtle()


shape.square(alex,120)

shape.rectangle(alex,80,40)

shape.octagon(alex,20)

alex.up()
alex.forward(-150)
alex.down()

shape.square(alex,80)


screen.exitonclick()
