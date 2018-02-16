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
FX
X -> X+YF+
Y -> -FX-Y
"""

def applyRules(ch):
    new_string = ""
    if ch == "X":
        new_string = "X+YF+"
    elif ch == "Y":
        new_string = "-FX-Y"
    else:
        new_string = ch

    return new_string

def turtle_draw(turtle, instructions, angle, steps):
    for char in instructions:

        if char == "X":
            turtle.forward(steps)
        elif char == "Y":
            turtle.forward(-steps)
        elif char == "+":
            turtle.right(angle)
        elif char == "-":
            turtle.left(angle)

instructions = LSystem(9, "FX")
print(instructions)

turtle_draw(alex, instructions, 90, 2)

screen.exitonclick()
