from turtle import Turtle

class TextWriter(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.font = ('Arial', 10, 'bold')

    def write_text(self, state_row):
        xcor = state_row.x.item()
        ycor = state_row.y.item()
        state_name = state_row.state.item()
        # print(state_name, xcor, ycor)
        
        self.goto(xcor, ycor)
        self.write(state_name, align='center', font=self.font)
