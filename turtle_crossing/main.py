import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            score_board.game_over()
            game_is_on = False

    if player.is_at_fin():
        car_manager.next_lvl()
        player.return_to_start()
        score_board.next_lvl()

    screen.listen()
    screen.onkey(player.move, "Up")


screen.exitonclick()



