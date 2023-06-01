#!/usr/bin/env python3
#Draw a spirograph using turtle python

import turtle
from turtle import Turtle, Screen
import random

rich_turtle = Turtle()
rich_turtle.speed("fastest")
turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        rich_turtle.color(random_color())
        rich_turtle.circle(100)
        rich_turtle.setheading(rich_turtle.heading() + size_of_gap)

draw_spirograph(5)


screen = Screen()
screen.bgcolor("black")
screen.exitonclick()
