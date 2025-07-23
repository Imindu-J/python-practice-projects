# import colorgram
#
# color_objects= colorgram.extract("image.jpg", 30)
# colors = []
#
# for color in color_objects:
#     color_as_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
#     colors.append(color_as_tuple)
#
# print(colors)

import turtle as t
import random

tim = t.Turtle()
tim.shape("classic")
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

colors= [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99), (122, 175, 156),
          (226, 198, 131), (192, 87, 108), (11, 50, 64), (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143),
          (168, 21, 29), (228, 92, 77), (244, 162, 160), (38, 32, 35), (2, 25, 24), (78, 147, 171), (170, 23, 18),
          (19, 79, 90), (101, 126, 158), (235, 166, 171), (177, 204, 185), (49, 62, 84)]

def row():
    for n in range(10):
        tim.dot(20, random.choice(colors))
        tim.fd(50)
    column()

def column():
    tim.left(90)
    tim.fd(50)
    tim.left(90)
    tim.fd(500)
    tim.left(180)

tim.setheading(225)
tim.fd(325)
tim.setheading(0)

for _ in range(10):
    row()

screen = t.Screen()
screen.exitonclick()