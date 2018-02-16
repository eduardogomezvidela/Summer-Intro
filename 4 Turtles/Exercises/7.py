#A drunk pirate makes a random turn and then takes 100 steps forward, makes another random turn, takes another 100 steps,
#turns another random amount, etc. A social science student records the angle of each turn before the next 100 steps are taken.
#Her experimental data is 160, -43, 270, -97, -43, 200, -940, 17, -86. (Positive angles are counter-clockwise.)
#Use a turtle to draw the path taken by our drunk friend. After the pirate is done walking, print the current heading.

import turtle
screen=turtle.Screen()
screen.bgcolor("black")
morgan=turtle.Turtle()
morgan.color("white")

for i in (160,-43,270,-97,-43,200,-940,17,-86):
    morgan.left(i)
    morgan.forward(100)

print("Final heading:", morgan.heading()) #morgan.heading() is used to determine the turtle's heading in degrees

screen.exitonclick()
