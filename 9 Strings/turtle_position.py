#Turtle L-System
import turtle
screen = turtle.Screen()
screen.bgcolor("black")
alex = turtle.Turtle()
alex.color("white")
alex.up()
alex.goto(-475,0)
alex.down()
alex.pensize(2)
alex.right(-60)
alex.forward(80)
print(alex.position())
print(alex.heading())

alex2 = turtle.Turtle()
alex2.color("green")
alex2.up()
alex2.down()
alex2.pensize(2)
alex2.goto(alex.position())     #Goes to first turtle's position
alex2.left(alex.heading())          #Faces same way as first turtle's direction
alex2.forward(50)
