from turtle import Turtle


# The Ball class
# Width = 20, height = 20, shape = circle, x_pos = 0, y_pos = 0
# Move the ball to the right top corner of the screen.

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("chartreuse")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Move the ball across the board."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Bounces the ball at virtically."""
        self.y_move *= -1

    def bounce_x(self):
        """Bounces the ball at horizontally."""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        """Resets the balls positions."""
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1