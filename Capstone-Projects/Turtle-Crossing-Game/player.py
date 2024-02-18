from turtle import Turtle

# Constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('darkgreen')
        self.penup()
        self.setheading(90)
        self.reset_position()

    def move(self):
        """Moves the player up."""
        self.forward(MOVE_DISTANCE)

    def is_touched_finish_line(self):
        """Returns true if the player touches the finish line."""
        return self.ycor() >= FINISH_LINE_Y

    def reset_position(self):
        """Resets turtle initial position."""
        self.goto(STARTING_POSITION)

    
