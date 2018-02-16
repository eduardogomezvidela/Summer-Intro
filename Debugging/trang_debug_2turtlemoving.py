import random
import turtle

def InScreen(w, t):                                 #Checks if turtle is still inside window, else stops turtles
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

def turtle_move(turtle):                            #Gives turtle its random moving instructions
    coin = random.randrange(0, 2)
    if coin == 0:
        turtle.left(90)
    else:
        turtle.right(90)
    turtle.forward(50)

wn = turtle.Screen()                #Set up turtles and window
tess = turtle.Turtle()
tess.color("red")
alex = turtle.Turtle()
alex.color("blue")

tess.up()                                   #Sets both turtles in random positions
alex.up()
tess.goto(random.randrange(-wn.window_width()/2, wn.window_width()/2), random.randrange(-wn.window_height()/2, wn.window_height()/2))
alex.goto(random.randrange(-wn.window_width()/2, wn.window_width()/2), random.randrange(-wn.window_height()/2, wn.window_height()/2))
tess.down()
alex.down()

while InScreen(wn, tess) and InScreen(wn,alex):         #Makes both turtles move as long as BOTH are inside window
    turtle_move(tess)
    turtle_move(alex)

