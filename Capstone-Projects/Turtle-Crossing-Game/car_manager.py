from turtle import Turtle
from random import choice, randint

# Constants.
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def create_car(self):
        """Create/Generate a new car."""
        chance = randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.color(choice(COLORS))
            new_car.setheading(180)
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(300, randint(-240, 240))
            self.all_cars.append(new_car)

    def move_cars(self):
        """Moves cars from the right eadge to left edge."""
        for car in self.all_cars:
            car.forward(self.car_speed)

    def increase_speed(self):
        """Increase the car move speed."""
        self.car_speed += MOVE_INCREMENT
        
