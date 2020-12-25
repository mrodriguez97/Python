from turtle import Turtle
import random
from datetime import datetime

random.seed(datetime.now())
MOVE_INCREMENT = 10
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Car(Turtle):
    def __init__(self, car_speed):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        random_y = random.randint(-250, 250)
        self.goto(300, random_y)
        self.setheading(180)
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.speed = car_speed

    def move_car(self):
        self.forward(self.speed)


