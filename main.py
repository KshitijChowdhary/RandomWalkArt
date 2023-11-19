import random
import turtle
from turtle import Turtle, Screen
from random import choice

tim = Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    colours = (r, g, b)
    return colours

#Turtle properties
tim.shape("turtle")
tim.color("red")

#Pen
tim.pendown()
tim.pensize(5)

#Lists

directions = [0, 90, 180, 270]

#Motion
for i in range(200):
    tim.forward(30)
    tim.setheading(random.choice(directions))
    tim.color(random_color())





























screen = Screen()
screen.exitonclick()