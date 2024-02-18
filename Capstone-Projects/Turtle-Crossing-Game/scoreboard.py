from turtle import Turtle

# Constants
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.hideturtle()
        self.level = 0
        self.goto(-230, 260)
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(f'Level: {self.level}', align='center', font=FONT)

    def increase_level(self):
        self.level += 1
        self.write_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over!', align='center', font=FONT)

