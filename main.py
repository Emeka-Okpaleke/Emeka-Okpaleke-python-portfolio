import turtle
import random
import colorgram
from turtle import Turtle, Screen

tim = Turtle()
turtle.colormode(255)

# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)

def row_movement():
    y = 0
    for _ in range(10):
        y += 10
        tim.pendown()
        tim.color(random.choice(color_list))
        tim.dot(10)
        tim.penup()
        tim.forward(50)
        tim.dot(10)
        tim.penup()


def new_position(y):
    tim.goto(0, y)
    tim.pendown()


color_list = [(134, 167, 191), (211, 156, 106), (197, 143, 166), (29, 110, 168), (234, 214, 86), (127, 74, 92),
              (187, 178, 19), (26, 136, 66), (55, 18, 26), (142, 20, 40), (38, 175, 113), (225, 170, 196),
              (116, 188, 144), (231, 77, 50), (172, 70, 46), (238, 218, 5), (37, 17, 16), (186, 91, 110), (9, 102, 52),
              (34, 167, 189), (20, 20, 28), (183, 185, 213), (234, 171, 159), (154, 215, 172), (142, 20, 16),
              (89, 124, 182)]

tim.speed(0)
y = 0
for _ in range(10):
    tim.speed(10)
    y += 20
    row_movement()
    tim.goto(0, y)

Screen().exitonclick()
