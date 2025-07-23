from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score} ", False, "left", font=FONT)

    def next_lvl(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", False, "center", font=FONT)
