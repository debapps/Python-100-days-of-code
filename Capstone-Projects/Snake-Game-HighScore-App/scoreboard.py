from turtle import Turtle

# Constants
SCORE_FONT = ('Courier', 18, 'normal')
GAME_FONT = ('Courier', 32, 'bold')
ALLIGNMENT = "center"
HIGH_SCORE_FILE = 'high_score.txt'

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.score = 0
        self.high_score = self.read_high_score()
        self.show()
        
    # Shows the score.
    def show(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALLIGNMENT, font=SCORE_FONT)

    # Update the score.
    def update_score(self):
        """Update the score."""
        self.score += 1
        self.show()

    # Reset the score and set the High Score instead of game over sequence.
    def reset_score(self):
        """Reset the score and set the High Score."""
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.show()

    # Read the high score from the file.
    def read_high_score(self):
        with open(HIGH_SCORE_FILE, mode='r') as high_score_file:
            data = high_score_file.read()

        return int(data)
    
    # Write High Score into the file.
    def write_high_score(self):
        with open(HIGH_SCORE_FILE, mode='w') as high_score_file:
            high_score_file.write(str(self.high_score))


        
