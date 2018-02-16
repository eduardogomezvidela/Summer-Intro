import LSystem
import turtle

screen = turtle.Screen()
screen.bgcolor('black')
alex = turtle.Turtle()
alex.color('darkgreen')

instructions = (LSystem.LSystem(4,'H'))
print(instructions)

#RULES:
"""
H
H --> HFX[+H][-H]
X --> X[-FFF][+FFF]FX
"""

def turtle_draw(turtle, instructions, steps, angle):
    position_list = ''
    heading_list = []
    x_position = []
    y_position = []
    for char in instructions:
        if char == 'F':
            turtle.forward(steps)
        elif char == '+':
            turtle.right(angle)
        elif char == '-':
            turtle.left(angle)
        elif char == '[':
            x_position = x_position + [turtle.xcor()]
            y_position = y_position + [turtle.ycor()]
            heading_list = heading_list + [turtle.heading()]
        elif char == ']':
            turtle.goto(x_position.pop(), y_position.pop())
            turtle.setheading(heading_list.pop())

alex.speed(0)
turtle_draw(alex, instructions, 10, 25.7)

screen.exitonclick()
