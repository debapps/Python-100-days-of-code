from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    # Initialize the Snake.
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Create the initial snake.
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    # Add a segment.
    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.shapesize(stretch_len=0.5, stretch_wid=0.5)
        segment.color("white")
        segment.penup()
        segment.setpos(position)
        self.segments.append(segment)

    # Extend the snake body.
    def extend(self):
        """Extend the snake body."""
        self.add_segment(self.segments[-1].position())
        
    # Move the snake forward.
    def move(self):
        """Move the snake forward."""
        for seg_idx in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[seg_idx - 1].pos()
            self.segments[seg_idx].setpos(new_pos)

        self.segments[0].forward(MOVE_DISTANCE)

    # Turn the snake up.
    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    # Turn the snake down.
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
    
    # Turn the snake left.
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    
    # Turn the snake right.
    def right(self):
         if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
