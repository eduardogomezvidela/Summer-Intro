import random
import turtle

def InScreen(w, t):
    lb = -w.window_width()/2
    rb = w.window_width()/2
    tb = w.window_height()/2
    bb = -w.window_height()/2
    
    corx = t.xcor()
    cory = t.ycor()
    
    stillIn = True
    if corx > rb or corx < lb or cory > tb or cory < bb:
        stillIn = False
    return stillIn

wn = turtle.Screen()
tess = turtle.Turtle()
tess.color("red")
alex = turtle.Turtle()
alex.color("blue")

for i in [tess, alex]:
    i.up()
    i.goto(random.randrange(-wn.window_width()/2, wn.window_width()/2), random.randrange(-wn.window_height()/2, wn.window_height()/2))
    i.down()
    while InScreen(wn, i):
        coin = random.randrange(0, 2)
        if coin == 0:
            i.left(90)
        else:
            i.right(90)
        i.forward(50)
