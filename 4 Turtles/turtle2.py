import turtle

wn = turtle.Screen()

color = input("BG color")

wn.bgcolor(color)        # set the window background color

tess = turtle.Turtle()

tess_color=input("Turtle color")

tess.color(tess_color)              # make tess a color

size_s=input("Pen size")
size=int(size_s)

tess.pensize(size)                 # set the width of her pen

tess.forward(50)
tess.left(120)
tess.forward(50)
tess.left(120)
tess.forward(50)

wn.exitonclick()                # wait for a user click on the canvas
