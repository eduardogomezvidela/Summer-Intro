#Draws bars and writes their length

import turtle
import math

def drawBarF(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape
    
def drawBarW(t, height):
    """ Writes height of each bar. """ 
    t.up()               
    t.hideturtle()
    t.left(90)
    t.forward(height)
    if (height >= 0):
        t.right(45)
        t.forward(3)
        t.write(str(height), font=("Arial", 12, "normal"))
        t.forward(-3)
        t.right(-45)
    elif (height < 0):
        t.forward(-height)
        t.right(45)
        t.forward(3)
        t.write(str(height), font=("Arial", 12, "normal"))
        t.forward(-3)
        t.right(-45)
        t.forward(height)  

    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)



xs = [48, -15, 200, 240, 160, 260, 220]  # here is the data
print(xs)
maxheight = max(xs)
numbars = len(xs)
border = 10

wn = turtle.Screen()             # Set up the window and its attributes
wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
wn.bgcolor("lightgreen")

tess = turtle.Turtle()           # create tess and set some attributes
tess.color("blue")
tess.pensize(3)
tess.speed(0)



for a in xs:
    if (a >= 200):
        tess.fillcolor("red")
    elif (a>=100):
        tess.fillcolor("yellow")
    elif (a<100):
        tess.fillcolor("green")
    drawBarF(tess, a)
    
    
tess.goto(0,0)
for a in xs:
    drawBarW(tess, a)

    
wn.exitonclick()
