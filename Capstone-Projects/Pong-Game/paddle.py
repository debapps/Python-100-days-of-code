from turtle import Turtle

MOVE_DISTANCE = 20

# The Paddle class.
# The Paddle moves up and down when up and down keys are pressed from the keyboard.
class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_pos, y_pos)

    # Moves the paddle upward.
    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    
    # Moves the paddle downward.
    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)