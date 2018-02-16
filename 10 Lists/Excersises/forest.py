import random_weed
import random
import turtle
import random_tree_LSystem
import random_grass

screen = turtle.Screen()
screen.bgcolor("black")
alex = turtle.Turtle()

turtle.tracer(0,0)
turtle.delay(0)

x = -400
y = -300



alex.up()
alex.goto(x,-300)
alex.down()
alex.hideturtle()

turtle.colormode(255)

red = 45
green = 206
yellow = 65

for color in range(10):                                                  #Grass
    alex.color(red,green,yellow)
    green = green - 17
    red = red - 4
    yellow = yellow - 4
    random_grass.grass(alex,screen, y)

    alex.up()
    y = y - 12
    alex.down()

    turtle.update()

alex.pensize(1)

turtle.colormode(1)
alex.color("darkgreen")

alex.up()
alex.goto(-500,-300)
alex.down()

while alex.xcor() < 500:
    random_weed.weed(alex,screen)
    x = x + random.randrange(50,121)
    alex.up()
    alex.goto(x,-300)
    alex.down()
    alex.right(90)
    turtle.update()

random_tree_LSystem.tree(alex,screen)

turtle.update()

screen.exitonclick()
