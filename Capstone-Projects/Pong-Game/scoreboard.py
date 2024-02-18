from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("gold")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.show()

    def show(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 70, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 70, "normal"))

    def update_l_score(self):
        """Updates the score for left player."""
        self.l_score += 1
        self.show()
    
    def update_r_score(self):
        """Updates the score for right player."""
        self.r_score += 1
        self.show()
