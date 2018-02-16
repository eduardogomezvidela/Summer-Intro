#Turtle L-System
import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
alex = turtle.Turtle()
alex.color("darkgreen")

alex.speed(0)
alex.hideturtle()
alex.pensize(2)
alex.left(90)
alex.up()
alex.forward(-200)
alex.down()

def LSystem (iterations,axiom):
    org_string = axiom                              #The org_string starts as the axiom that we input
    new_string= ''

    for i in range (iterations):                        #This will make our new_string update itself accordingly and the right amount of times
        new_string = process(org_string)
        org_string = new_string

    return new_string

def process(org_string): #This will need to iterate through each char in the org_string, return a new_string and call the rules
    new_string = ''
    
    for char in org_string:
        new_string = new_string + applyRules(char)

    return new_string

def applyRules(ch):
    newstr = ""
    if ch == '1':
        newstr = '11'   # Rule 1
    elif ch == '0':
        newstr = '1-0+0'
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def turtle_draw(turtle, instructions, angle, steps):
    pos = []
    ang= []
    for char in instructions:

        if char == '1':
            turtle.forward(steps)

        elif char == '0':
            turtle.forward(steps)
            turtle.forward(-steps)
            
        elif char == '-':
            pos.append(turtle.position())
            ang.append(turtle.heading())
            turtle.left(angle)

        elif char == '+':
            turtle.up()
            turtle.goto(pos.pop())
            turtle.setheading(ang.pop())
            turtle.right(angle)
            turtle.down()




formula = LSystem(6,'0')
print(formula)


turtle_draw(alex,formula,45,8)

#alex2.goto(alex.position())     #Goes to first turtle's position
#alex2.setheading(alex.heading())          #Faces same way as first turtle's direction


screen.exitonclick()

