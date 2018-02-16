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
X -> X+YF++YF-FX--FXFX-YF+
Y -> -FX+YFYF++YF+FX--FX-Y
"""

def applyRules(ch):
    new_string = ""
    if ch == "X":
        new_string = "X+YF++YF-FX--FXFX-YF+"
    elif ch == "Y":
        new_string = "-FX+YFYF++YF+FX--FX-Y"
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

instructions = LSystem(3, "YF")
print(instructions)

turtle_draw(alex, instructions, 60, 5)

screen.exitonclick()
