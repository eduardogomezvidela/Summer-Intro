#Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):
#An equilateral triangle
#A square
#A hexagon (six sides)
#An octagon (eight sides)

import turtle
screen=turtle.Screen()
screen.bgcolor("white")
alex=turtle.Turtle()
alex.speed(10)

alex.up()
alex.goto(-300,350)

alex.down()                         #Alex draws the triangle
alex.right(60)
for i in(1,2,3):
    alex.forward(200)
    alex.right(120)

alex.up()
alex.goto(0,350)
alex.down()

alex.left(60)
for i in(1,2,3,4):                #Alex draws the square
    alex.forward(170)
    alex.right(90)

alex.up()
alex.goto(-300,0)
alex.down()

for i in range(6):
    alex.forward(100)            #Alex draws the hex
    alex.right(60)

alex.up()
alex.goto(0,0)
alex.down()

for i in range(8):                    #Alex draws the octa
    alex.forward(75)
    alex.right(45)

screen.exitonclick()
