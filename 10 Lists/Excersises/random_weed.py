import LSystem
import turtle
import random

def weed(turtle, screen):

    instructions = (LSystem.LSystem(4,'H'))
    print(instructions)

    #RULES:
    """
    H
    H --> HFX[+H][-H]
    X --> X[-FFF][+FFF]FX
    """

    def turtle_draw(turtle, instructions, steps, angle):
        instructions = (LSystem.LSystem(4,'H'))
        turtle.speed(0)
        turtle.left(90)
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

    rand = random.randrange(10,50,1)
    rand = rand / 10
    print(rand)
    rand2 = random.randrange(15,45)
    turtle_draw(turtle, instructions, rand, rand2)
