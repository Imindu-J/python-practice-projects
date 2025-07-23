from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.return_to_start()

    def move(self):
        self.fd(MOVE_DISTANCE)

    def is_at_fin(self):
        if self.ycor() > FINISH_LINE_Y:
            return True

    def return_to_start(self):
        self.goto(STARTING_POSITION)
