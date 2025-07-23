from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PingPong")
screen.tracer(0)

paddle_l = Paddle((-350, 0))
paddle_r = Paddle((350, 0))
ball = Ball()
score_board = ScoreBoard()


game_on = True
while game_on:
    screen.update()
    time.sleep(ball.delay)
    ball.move()

    # Ball hits top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    # Ball hits paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.delay *= 0.9
        time.sleep(ball.delay)

    # paddle_r misses
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.increase_lscore()

    # paddle_l misses
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.increase_rscore()

    screen.listen()
    screen.onkey(paddle_l.up, "w")
    screen.onkey(paddle_l.down, "s")
    screen.onkey(paddle_r.up, "Up")
    screen.onkey(paddle_r.down, "Down")


screen. exitonclick()
