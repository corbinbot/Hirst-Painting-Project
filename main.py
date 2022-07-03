import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)

puji = Turtle()
puji.shape("turtle")
puji.penup()
puji.goto(-200, -200)
puji.pendown()



color_listwa = [(199, 175, 117), (124, 36, 24), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]

pos = 0
for i in range(10):
    puji.goto(-200, -200 + pos)

    for i in range(10):
        acha_color = (random.choice(color_listwa))
        puji.speed(30)
        puji.pencolor(acha_color)
        puji.dot(20)

        puji.penup()
        puji.forward(50)

    pos += 50







screen = Screen()
screen.exitonclick()