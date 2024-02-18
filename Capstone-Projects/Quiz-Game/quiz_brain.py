
class QuizBrain:
    def __init__(self, question_bank) -> None:
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    # Checks if the question bank still remaining questions to ask.
    def still_has_questions(self):
        return len(self.question_list) > self.question_number
        # if len(self.question_list) > self.question_number:
        #     return True
        # else:
        #     return False

    # Get the next question and check the user answer.
    def next_question(self):
        current_qustion = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"\nQ.{self.question_number}: {current_qustion.text} (True/False)?: ")
        self.check_answer(user_answer, current_qustion.answer)

    # Check the user answer and evaluate the user score.
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")

        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
