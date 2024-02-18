import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title('Turtle Crossing Game')

# Get the turtle.
timmy = Player() 

# Create the car manager objects.
car_manager = CarManager()

# Get the score board.
score = Scoreboard()

# Screen listen to the event listeners
screen.listen()
screen.onkey(key='Up', fun=timmy.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Generate cars and move them.
    car_manager.create_car()
    car_manager.move_cars()

    # Detect a collition between player and cars.
    for car in car_manager.all_cars:
        if car.distance(timmy) < 20:
            score.game_over()
            game_is_on = False

    # Detect when playes reaches the finish line.
    if timmy.is_touched_finish_line():
        score.increase_level()
        car_manager.increase_speed()
        timmy.reset_position()
    

   

screen.exitonclick()


    
