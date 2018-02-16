import turtle

bg = turtle.Screen()
bg_input = input("Background color?")
bg.bgcolor(bg_input)

alex = turtle.Turtle()
alex_input = input("Turtle color?")
alex.color(alex_input)
alex.pensize(15)

step=1

for i in range(100):
    print("Step", step)

    instructions = input("left, right, forward, penup or pendown?")

    if instructions ==("left"):
        turn_str=input("How many degrees?")
        turn=int(turn_str)
        alex.left(turn)

    if instructions ==("right"):
        turn_str=input("How many degrees?")
        turn=int(turn_str)
        alex.right(turn)

    if instructions ==("forward"):
        distance_str = input("How many steps to take?")
        distance = int(distance_str)
        alex.forward(distance)

    if instructions==("penup"):
        alex.penup()

    if instructions==("pendown"):
        alex.pendown()

    step=step+1


bg.exitonclick()
