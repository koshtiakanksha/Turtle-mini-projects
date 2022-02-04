import turtle
from turtle import Turtle, Screen
import random
import colorgram

tim = Turtle()
tim.shape("turtle")
tim.pensize(5)
turtle.colormode(255)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def shapes():
    def polygon(x):
        for _ in range(x):
            tim.forward(100)
            tim.right(360/x)
    for i in range(3, 11):
        tim.color(random_color())
        polygon(i)


def random_walk():
    tim.speed(1000)
    for i in range(100):
        tim.forward(random.choice(range(10, 50, 10)))
        tim.color(random_color())
        tim.setheading(random.choice(range(90, 450, 90)))


def spirograph():
    tim.pensize(1)
    for i in range(72):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+5)


colors = colorgram.extract("download.jpg", 15)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
clrs = [(237, 224, 80), (205, 4, 73), (236, 50, 130), (198, 164, 8), (111, 179, 218),
        (204, 75, 12), (219, 161, 103), (234, 224, 4), (11, 23, 63), (29, 189, 111), (22, 107, 174)]


def hirst_painting():
    tim.hideturtle()
    tim.setheading(225)
    tim.penup()
    tim.forward(250)
    tim.setheading(0)
    tim.pendown()
    for i in range(10):
        for j in range(10):
            tim.dot(20, random.choice(clrs))
            tim.penup()
            tim.forward(50)
            tim.pendown()
        tim.setheading(90)
        tim.penup()
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
        tim.pendown()


# shapes()
# random_walk()
# spirograph()
# hirst_painting()
# uncomment one function at a time to see results
screen = Screen()
screen.exitonclick()
