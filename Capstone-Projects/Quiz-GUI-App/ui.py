from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUIZ_FONT = ('Arial', 20, 'italic')
SCORE_FONT = ('Courier', 16, 'bold')

class QuizGUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0

        #----------------------- UI Setup -----------------------#
        self.window = Tk()
        self.window.title('Quiz App')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Score level.
        self.score_label = Label(self.window, text=f'Score: {self.score}', 
                                bg=THEME_COLOR, fg='white', font=SCORE_FONT)
        

        # Quiz Canvas.
        self.quiz_screen = Canvas(self.window, height=250, width=300, bg='white')
        self.quiz_text = self.quiz_screen.create_text((150, 125),
                         text='', fill=THEME_COLOR, font=QUIZ_FONT, width=280)
        

        # Photo Images
        tick_image = PhotoImage(file='./images/true.png')
        cross_image = PhotoImage(file='./images/false.png')

        # Buttons.
        self.true_btn = Button(self.window, image=tick_image, 
                        highlightthickness=0, command=self.answer_true)
        self.false_btn = Button(self.window, image=cross_image, 
                        highlightthickness=0, command=self.answer_false)

        # Geometry Manager Methods.
        self.score_label.grid(row=0, column=1)
        self.quiz_screen.grid(row=1, column=0, columnspan=2, pady=50)
        self.true_btn.grid(row=2, column=0, padx=10)
        self.false_btn.grid(row=2, column=1, padx=10)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.quiz_screen.config(bg='white')
        self.score_label.config(text=f'Score: {self.quiz.score}')
        if self.quiz.still_has_questions():
            new_question = self.quiz.next_question()
            self.quiz_screen.itemconfig(self.quiz_text, text=new_question)
        else:
            self.quiz_screen.itemconfig(self.quiz_text, text=f'Finished All Questions!!\nYour Final Score: {self.quiz.score}')
            self.true_btn.config(state=DISABLED)
            self.false_btn.config(state=DISABLED)


    def answer_true(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)
    
    def answer_false(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            color = 'green'
        else:
            color = 'red'

        self.quiz_screen.config(bg=color)

        self.feedback_timer = self.window.after(1000, self.get_next_question)
        

        
        


