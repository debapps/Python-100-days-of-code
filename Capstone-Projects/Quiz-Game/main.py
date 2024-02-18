from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

def quiz_game():

    # Creating the question bank.
    question_bank = []
    for question in question_data:
        question_object = Question(question['question'], question['correct_answer'])
        question_bank.append(question_object)
    
    # Create the quiz brain object.
    quiz = QuizBrain(question_bank)

    # Getting all the questions.
    while quiz.still_has_questions():
        quiz.next_question()

    print("You've completed the quiz.")
    print(f"Your final score was: {quiz.score}/{len(question_bank)}")

if __name__ == "__main__":
    quiz_game()