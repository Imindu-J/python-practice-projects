import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
tim.speed("fastest")
t.colormode(255)


def rand_color():
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    return (R, G, B)

def draw_spirograph(gap):
    for a in range(int(360/gap)):
        tim.color(rand_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap)

draw_spirograph(1)




screen = t.Screen()
screen.exitonclick()