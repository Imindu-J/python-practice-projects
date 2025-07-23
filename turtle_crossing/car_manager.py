from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():

    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.color(choice(COLORS))
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(300, randint(-230, 230))
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.move_distance)

    def next_lvl(self):
        self.move_distance += MOVE_INCREMENT




