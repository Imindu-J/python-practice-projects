from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.center_line()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scores()

    def center_line(self):
        self.penup()
        self.goto(x=0, y=-300)
        self.setheading(90)
        for n in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def update_scores(self):
        self.goto(x=0, y=220)
        self.write(f"{self.l_score} {self.r_score}", move=False, align="center", font=("Courier", 50, "bold"))

    def increase_lscore(self):
        self.l_score += 1
        self.clear()
        self.center_line()
        self.update_scores()

    def increase_rscore(self):
        self.r_score += 1
        self.clear()
        self.center_line()
        self.update_scores()