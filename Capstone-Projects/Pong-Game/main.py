# The Pong Game.
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep

# Constants.
WALL = 280

# Set the screen.
pong_screen = Screen()
pong_screen.bgcolor("black")
pong_screen.setup(width=800, height=600)
pong_screen.title("The Pong Game")

# Turn off screen annimation.
pong_screen.tracer(0)

# Get the left and right paddles.
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

# Get the ball
pong = Ball()

# Get the scoreboard.
scoreboard = Scoreboard()

# Set the event listeners.
pong_screen.listen()
pong_screen.onkey(key="Up", fun=r_paddle.move_up)
pong_screen.onkey(key="Down", fun=r_paddle.move_down)
pong_screen.onkey(key="w", fun=l_paddle.move_up)
pong_screen.onkey(key="s", fun=l_paddle.move_down)

game_on = True

while game_on:
    # Set the ball move speed
    sleep(pong.move_speed)

    # Turn on screen annimation.
    pong_screen.update()
    
    # Ball started to move.
    pong.move()

    # Detect the collision of the ball with the top and down walls and bounce when collides.
    if pong.ycor() > WALL or pong.ycor() < -1 * WALL:
        pong.bounce_y()

    # Detect the collision of the ball with the paddle.
    if (pong.xcor() > 320 and pong.distance(r_paddle) < 50) or (pong.xcor() < -320 and pong.distance(l_paddle) < 50):
        pong.bounce_x()

    # Detect if the R paddle misses the ball.
    if pong.xcor() > 380 :
        scoreboard.update_l_score()
        pong.reset()
    
    # Detect if the L paddle misses the ball.
    if pong.xcor() < -380 :
        scoreboard.update_r_score()
        pong.reset()

pong_screen.exitonclick()
