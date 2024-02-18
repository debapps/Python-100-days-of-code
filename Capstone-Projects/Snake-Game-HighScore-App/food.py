from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.4, stretch_wid=0.4)
        self.color("yellow")
        self.penup()
        self.speed("fastest")
        self.place_food()

    # Place the food at random position on screen.
    def place_food(self):
        """Place the food at random position on screen."""
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
