#Turtle L-System
import turtle
import random

def tree(turtle,screen):
    
    alex = turtle

    alex.speed(0)
    alex.hideturtle()
    alex.pensize(2)
    alex.left(90)

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

    def turtle_draw(turtle, instructions):
        pos = []
        ang= []

        for char in instructions:
            angle = random.randrange(15,36)
            steps = random.randrange(2,7)
                
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
                turtle.down()
                    
                turtle.setheading(random.randrange(75,96))
                turtle.forward(random.randrange(3,8))
                turtle.setheading(ang.pop())
                turtle.right(angle)

    locator = -300

    for i in range (3):
        
        alex.up()
        alex.goto(locator,-300)
        alex.down()

        formula = LSystem(7,'0')

        turtle_draw(alex,formula)

        locator = locator + 300
        alex.setheading(90)
