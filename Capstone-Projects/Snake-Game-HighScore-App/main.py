# This is classic snake game.

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

WALL = 298
FOOD_DISTANCE = 10
TAIL_DISTANCE = 8

# Set the initial screen property.
screen = Screen()

# Set the screen title.
screen.title("Snake Game")

# Set screen width and height.
screen.setup(width=600, height=600)

# Set the screen color.
screen.bgcolor("Black")

# Set the screen annimation off.
screen.tracer(0)

# Get the snake object.
nagini = Snake()

# Get the food object.
kecho = Food()

# Get the scoreboard object.
score = Scoreboard()

# Set the event listeners. Set the function for up, down, left and right arrows in the keyboard.
screen.listen()
screen.onkey(key="Up", fun=nagini.up)
screen.onkey(key="Down", fun=nagini.down)
screen.onkey(key="Left", fun=nagini.left)
screen.onkey(key="Right", fun=nagini.right)

game_is_on = True
while game_is_on:
    # Show the screen annimation with 0.1 milli-second delay.
    screen.update()
    time.sleep(0.1)
    
    # start moving the snake.
    nagini.move()
    

    # Detect the collision of snake with food.
    if nagini.head.distance(kecho) < FOOD_DISTANCE:
        score.update_score()
        kecho.place_food()
        nagini.extend()

    # Detect the collision of snake with wall.
    if nagini.head.xcor() > WALL or nagini.head.xcor() < -1 * WALL or nagini.head.ycor() > WALL or nagini.head.ycor() < -1 * WALL:
        # game_is_on = False
        nagini.reset()
        score.reset_score()

    # Detect the collision of snake with its tail.
    # If the snake head collides with own body (one of the segments)
    for body in nagini.segments[1:]:
        if nagini.head.distance(body) < TAIL_DISTANCE:
            # game_is_on = False
            nagini.reset()
            score.reset_score()

# Show the screen until exit button is clicked.
screen.exitonclick()
