import turtle

wn = turtle.Screen()
pax = turtle.Turtle()

sides = int(input("How many sides does your polygon has?"))

length = int(input("How long is each side?"))

sidecolor = input("What is the color of the sides?")

fillcolor = input("What color is your polygon?")

print(360/sides)

for i in range (sides):
    pax.forward(length)
    pax.left(360/sides)
