#polygon and circle

import turtle

def drawPolygon(t, sideLength, numSides):       #Define polygon
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.right(turnAngle)

def drawCircle(anyTurtle, radius):                      #Define circle using polygon

    anyTurtle.begin_fill()

    #Positioning
    anyTurtle.up()
    anyTurtle.forward(radius)
    anyTurtle.right(90)
    anyTurtle.down()

    #Drawing
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    drawPolygon(anyTurtle, sideLength, 360)

    #Positioning
    anyTurtle.up()
    anyTurtle.right(-90)
    anyTurtle.forward(-radius)
    anyTurtle.down()
    anyTurtle.end_fill()


wn = turtle.Screen()
wheel = turtle.Turtle()

drawCircle(wheel, 20)                   #Call circle

wn.exitonclick()
