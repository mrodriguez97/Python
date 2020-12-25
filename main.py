import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def collision(play, car_list):
    crash = False
    for car in car_list:
        if play.distance(car) <= 20:
            crash = True
    return crash


screen = Screen()
screen.title("Frogger")
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.move_up)
screen.onkey(key="Down", fun=player.move_down)
screen.onkey(key="Left", fun=player.move_left)
screen.onkey(key="Right", fun=player.move_right)


game_is_on = True
count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.ycor() >= 290:
        player.reset_turtle()
        #manager.reset_list()
        manager.increase_speed()
        score.level_up()
        score.display_level()
        print(manager.car_speed)

    if count == 2:
        manager.create_car()
        count = 0

    if collision(player, manager.car_list):
        game_is_on = False
        score.game_over()

    manager.move_cars()

    count += 1

screen.exitonclick()
