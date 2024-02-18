from turtle import Turtle

# Constants
SCORE_FONT = ('Courier', 18, 'normal')
GAME_FONT = ('Courier', 32, 'bold')
ALLIGNMENT = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.score = 0
        self.show()
        
    # Shows the score.
    def show(self):
        self.write(f"Score: {self.score}", move=False, align=ALLIGNMENT, font=SCORE_FONT)

    # Update the score.
    def update_score(self):
        """Update the score."""
        self.score += 1
        self.clear()
        self.show()

    # Show the game over message.
    def show_game_over(self):
        """Show the game over message."""
        self.goto(0, 0)
        self.write("Game Over!", move=False, align=ALLIGNMENT, font=GAME_FONT)

        
