#L-System

#process axiom
#apply to new string

import turtle
screen = turtle.Screen()
alex = turtle.Turtle()
alex.speed(0)

def LSystem(iterations,axiom):

    old_string = axiom
    new_string=""

    for i in range(iterations):
        new_string = process(old_string)
        old_string = new_string

    return new_string

def process(old_string):
    new_string = ""

    for char in old_string:
        new_string = new_string + applyRules(char)

    return new_string


"""
L
L -> +RF-LFL-FR+
R -> -LF+RFR+FL-
"""

def applyRules(ch):
    new_string = ""
    if ch == "L":
        new_string = "+RF-LFL-FR+"
    elif ch == "R":
        new_string = "-LF+RFR+FL-"
    else:
        new_string = ch

    return new_string

def turtle_draw(turtle, instructions, angle, steps):
    for char in instructions:

        if char == "F":
            turtle.forward(steps)
        elif char == "B":
            turtle.forward(-steps)
        elif char == "+":
            turtle.right(angle)
        elif char == "-":
            turtle.left(angle)

instructions = LSystem(4, "L")
print(instructions)

turtle_draw(alex, instructions, 90, 5)

screen.exitonclick()
