from tkinter import *

THEME_COLOR = "#375362"

class QuizGUI:

    def __init__(self):
        self.window = Tk()
        self.window.title('Quiz App')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        
        self.quizScreen = Canvas(self.window, height=250, width=300, bg='white')
        self.quizScreen.pack()

        self.window.mainloop()
