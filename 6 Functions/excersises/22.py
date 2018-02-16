#Write a function called fancySquare that will draw a square with fancy corners (sprites on the corners).
#You should implement and use the drawSprite function from above.
#For an even more interesting look, how about adding small triangles to the ends of the sprite legs.


import turtle
import draw_sprite
screen=turtle.Screen()
screen.bgcolor("black")
alex=turtle.Turtle()
alex.color("white")
alex.speed(15)

for i in range(4):
    draw_sprite.draw_sprite(alex,25,8, 5, 8)
    alex.forward(300)
    alex.left(90)
    
screen.exitonclick()
