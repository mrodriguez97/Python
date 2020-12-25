from turtle import Turtle
from Car import Car

MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.car_speed = MOVE_INCREMENT

    def move_cars(self):
        for car in self.car_list:
            car.move_car()

            if car.xcor() <= -350:
                self.car_list.remove(car)

    def create_car(self):
        new_car = Car(self.car_speed)
        self.car_list.append(new_car)

    def reset_list(self):
        for car in self.car_list:
            car.reset()

        self.car_list.clear()
        self.increase_speed()

    def increase_speed(self):
        self.car_speed += 10
