#!/usr/bin/python3

import turtle as turtle_module
import random
turtle_module.colormode(255)
rich = turtle_module.Turtle()
rich.hideturtle()
rich.speed("fastest")
rich.penup()
color_list = [(140, 176, 207), (25, 32, 48), (26, 107, 159), (237, 225, 235), (209, 161, 111), (144, 29, 63), (230, 212, 93), (4, 163, 197), (218, 60, 84), (229, 79, 43), (195, 130, 169), (54, 168, 114), (28, 61, 116), (172, 53, 95), (108, 182, 90), (110, 99, 87), (193, 187, 46), (240, 204, 2), (1, 102, 119), (19, 22, 21), (50, 150, 109), (172, 212, 172), (118, 36, 34), (221, 173, 188), (227, 174, 166), (153, 205, 220), (184, 185, 210)]

rich.setheading(225)
rich.forward(300)
rich.setheading(0)
numbers_of_dots = 101

for dot_count in range(1, numbers_of_dots):
    rich.dot(20, random.choice(color_list))
    rich.forward(50)

    if dot_count % 10 == 0:
        rich.setheading(90)
        rich.forward(50)
        rich.setheading(180)
        rich.forward(500)
        rich.setheading(0)



screen = turtle_module.Screen()
screen.bgcolor("black")
screen.exitonclick()
