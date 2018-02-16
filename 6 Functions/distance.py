#calculates distance between two points on an x,y graph using the pythagoras theorem
#a**2+b**2=c**2         OR        squareroot(a**2 +b**2) = c

#all coordinates must be between -10 and 10

import turtle
import math
import axis

screen=turtle.Screen()
screen.bgcolor("black")
screen.setworldcoordinates(-11,-11,11,11)
alex=turtle.Turtle()
alex.color("white")
alex.pensize(3)
#alex.hideturtle()
bob=turtle.Turtle()
bob.color("hotpink")
bob.pensize(1)
bob.hideturtle()

def mark(turtle,a,b):
    turtle.up()
    turtle.goto(a,b)
    turtle.dot()

#Plot x y axis
axis.axis(-11,-11,11,11)

#Get all user input
point1x=input("Point 1 x coordinate:")              
point1x=int(point1x)

point1y=input("Point 1 y coordinate:")
point1y=int(point1y)

point2x=input("Point 2 x coordinate:")
point2x=int(point2x)

point2y=input("Point 2 y coordinate:")
point2y=int(point2y)

#Alex turtle marks both points
mark(alex,point1x,point1y)
alex.goto(point1x+0.2,point1y)
alex.write(point1x)
alex.goto(point1x+0.4,point1y)
alex.write(",")
alex.goto(point1x+0.5,point1y)
alex.write(point1y)

mark(alex,point2x,point2y)
alex.goto(point2x+0.2,point2y)
alex.write(point2x)
alex.goto(point2x+0.4,point2y)
alex.write(",")
alex.goto(point2x+0.5,point2y)
alex.write(point2y)

#Bob turtle connects the two dots with a line
bob.up()
bob.goto(point1x,point1y)
bob.down()
bob.goto(point2x,point2y)
bob.up()

#To get the value of each side we do:

sidex=point2x-point1x
sidex=abs(sidex)        #Absolute value (distance can't be negative)

sidey=point2y-point1y
sidey=abs(sidey)        #Absolute value (distance can't be negative)

#does the pythagoras theorem and calculates the distance from the two points
distance=math.sqrt(sidex**2+sidey**2)       

#Will print the distance on the top right of the screen
mich=turtle.Turtle()
mich.color("orange")
mich.hideturtle()
mich.up()
mich.goto(8,10.5)
mich.write(distance)

#Will print the distance on the terminal
print ("The distance between the two points is", distance)


##################################
alex.speed(0.3)
if (point1x == point2x):                    #for a 90 degreecase
    alex.left(90)
    if(point1y>point2y):
        alex.forward(distance/2)
    elif(point1y<point2y):
        alex.forward(-distance/2)
else:
    willy=sidey/sidex
    print(willy)

    angle=math.atan(willy)
    angle=math.degrees(angle)
    print(angle)

    alex.goto(point2x,point2y)

    alex.left(angle)

    if(point2x>point1x or point2y>point1y):
        alex.forward(-distance/2)

    else:
        alex.forward(distance/2)

    if(point2x>point1x or point2y>point1y):
        alex.forward(-distance/2)

if(point1y == point2y):
    if(point1x>point2x):
        alex.forward(distance/2)
    elif(point1x<point2x):
        alex.forward(-distance/2)
####################################

alex.write(distance)


screen.exitonclick()
