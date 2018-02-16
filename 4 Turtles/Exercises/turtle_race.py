import turtle              # 1.  import the modules
import random
wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3.  Create two turtles
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                  # 4.  Move the turtles to their starting point
lance.up()
andy.goto(-100,60)
lance.goto(-100,-40)

for i in range(100):# your code goes here
    x=random.randrange(1,10)    #5. Forward movement
    y=random.randrange(1,10)
    andy.forward(x)
    lance.forward(y)
    
    m=random.randrange(-5,6)    #5. Forward movement
    n=random.randrange(-5,6)
    andy.left(m)
    lance.left(n)

wn.exitonclick()
