#draws squares inside of squares

#each square is 20 units bigger than the previous one
#first square is 20 units

import turtle
screen=turtle.Screen()
screen.bgcolor("lightgreen")
alex=turtle.Turtle()
alex.color("hotpink")
alex.pensize(3)

import draw_square

square=20

for i in range(5):
    draw_square.draw_square(alex,square)
    square=square+20
    alex.up()
    alex.forward(-10)
    alex.left(90)
    alex.forward(10)
    alex.right(90)
    alex.down()






screen.exitonclick()
