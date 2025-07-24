from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        try:
            with open("data.txt") as data:
                content = data.read().strip()
                if content == "":
                    self.high_score = 0
                else:
                    self.high_score = int(content)
        except FileNotFoundError:
            with open("data.txt", mode="w") as data:
                data.write("0")
            self.high_score =  0
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.color("white")
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}. Highscore: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)
    #
