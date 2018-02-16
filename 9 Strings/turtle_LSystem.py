#Turtle L-System
import turtle
screen = turtle.Screen()
screen.bgcolor("black")
alex = turtle.Turtle()
alex.color("white")
alex.up()
alex.goto(-475,0)
alex.down()
alex.speed(0)
alex.hideturtle()
alex.pensize(2)

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
    if ch == 'F':
        newstr = 'F-F++F-F'   # Rule 1
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def turtle_draw(turtle, instructions, angle, steps):
    for char in instructions:
        if char == 'F':
            turtle.forward(steps)
        elif char == 'B':
            turtle.forward(-steps)
        elif char == '-':
            turtle.left(angle)
        elif char == '+':
            turtle.right(angle)

turtle_draw(alex,LSystem(5,'F'),60,4)
alex.right(180)
turtle_draw(alex,LSystem(5,'F'),60,4)


screen.exitonclick()
