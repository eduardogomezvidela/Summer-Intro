#3n+1

import turtle
import axis

screen=turtle.Screen()
screen.bgcolor("black")
bobby=turtle.Turtle()
bobby2=turtle.Turtle()

turtle.tracer(10)                       #Slightly speeds up the animation

screen.setworldcoordinates(-5,-5,55,120)

axis.axis(-10,-10,55,120)               #draw axis

bobby.color("green")
bobby.up()
bobby.hideturtle()

for i in range(1,51):                       #label x coordinates
    bobby.goto(i,-2)
    bobby.write(i)

bobby2.color("green")
bobby2.up()
bobby2.hideturtle()

for i in range(0,121,5):                    #label y coordinates
    bobby2.goto(-2,i)
    bobby2.write(i)

alex=turtle.Turtle()
alex.color("white")
alex.speed(0)
alex.hideturtle()
alex.up()

counter = 0
max = counter

for x in range (1, 51):                         #draw line (should actually be points and not a line)
    old_x=x
    print("----------------")
    print(x)

    while (x != 1):
        if (x % 2 == 0): #even
            x = x / 2
        else:                   #odd
            x = (x * 3)+1

        counter = counter + 1
        #print(x)

        if (counter > max):                 #searches for max counter
            max = counter

    print("Count: ", counter)
    alex.goto(old_x,counter)
    alex.dot()

    counter=0

print(max)                      #max counter


screen.exitonclick()
