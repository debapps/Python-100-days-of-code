# This is Etch-A-Sketch game application using turtle graphics.
from turtle import Turtle, Screen

MOVE = 10
TURN = 10

# Create the turtle and screen objects.
pen = Turtle()
canvas = Screen()

canvas.title("Etch-A-Sketch App")


# Listen to the screen events.
canvas.listen()

# Drags pen forward.
def move_forward():
    pen.forward(MOVE)

# Drags pen backward.
def move_back():
    pen.back(MOVE)

# Turn right.
def turn_right():
    pen.right(TURN)

# Turn left.
def turn_left():
    pen.left(TURN)

def clear_screen():
    pen.penup()
    pen.clear()
    pen.home()
    pen.pendown()

# Event listeners.
canvas.onkey(key="w", fun=move_forward)
canvas.onkey(key="Up", fun=move_forward)
canvas.onkey(key="s", fun=move_back)
canvas.onkey(key="Down", fun=move_back)
canvas.onkey(key="a", fun=turn_left)
canvas.onkey(key="Left", fun=turn_left)
canvas.onkey(key="d", fun=turn_right)
canvas.onkey(key="Right", fun=turn_right)
canvas.onkey(key="c", fun=clear_screen)

# Exit app on click.
canvas.exitonclick()