from turtle import Turtle, Screen
import random

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
turtles = []
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win? Enter a color: ")

for n in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[n])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=90 - (30 * n))
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()

            if user_bet == winner:
                print(f"You've won! The {winner} is the winner.")
            else:
                print(f"You've lost! The {winner} is the winner.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
