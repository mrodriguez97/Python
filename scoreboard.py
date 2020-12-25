from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.level = 1
        self.goto(-280, 250)
        self.display_level()

    def display_level(self):
        self.clear()
        self.write(f"LeveL: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)



