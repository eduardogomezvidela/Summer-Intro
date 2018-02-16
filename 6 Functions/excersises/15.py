import turtle
import draw_star

screen=turtle.Screen()
screen.bgcolor("black")
alex=turtle.Turtle()
alex.color("white")
alex.speed(3)
alex.pensize(3)
alex.up()
alex.forward(-300)
alex.down()

for i in range(5):
    draw_star.draw_star(alex,100)
    alex.up()
    alex.forward(350)
    alex.right(144)
    alex.down()










screen.exitonclick()
