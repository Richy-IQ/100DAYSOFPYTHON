#!/usr/bin/env python3
"""Constructing my sketch keys"""

from turtle import Turtle, Screen
rich = Turtle()
screen = Screen()

def move_forward():
 rich.forward(10)

def move_backward():
 rich.backward(10)

def turn_left():
 new_heading = rich.heading() + 10
 rich.setheading(new_heading)

def turn_right():
  new_heading = rich.heading() - 10
  rich.setheading(new_heading)


def clear():
 rich.clear()
 rich.penup()
 rich.home()
 rich.pendown()

screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.listen( )
screen.exitonclick()

