#Turtle L-System
import turtle
import random

def grass(turtle, screen, y_point):
    
    alex = turtle

    alex.speed(0)
    alex.hideturtle()
    alex.pensize(1)



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
        if ch == '0':
            newstr = '1-0+0'
        else:
            newstr = ch    # no rules apply so keep the character

        return newstr

    def turtle_draw(turtle, instructions, angle, steps):
        for char in instructions:
            if char == '1':
                turtle.forward(steps)
            elif char == '0':
                turtle.forward(steps)
                turtle.forward(-steps)
            elif char == '-':
                turtle.left(angle)
            elif char == '+':
                turtle.right(angle)

    x = -500

    for i in range(1000):
        ran = random.randrange(1,2)
        angle = random.randrange(-50,50,4)
        steps = random.randrange(3,10)

        formula = LSystem(ran,'0')

        alex.left(90)

        randomizer = random.randrange(-25,26)
        alex.left(randomizer)

        x = x + random.randrange(0,3)
        alex.up()
        alex.goto(x,y_point)
        alex.down()

        turtle_draw(alex,formula,angle,steps)

        alex.right(randomizer)

        alex.right(90)



    
