from flask import Flask
from random import randint

app = Flask(__name__)

RANDOM_NUMBER = None

@app.route("/")
def home():
    global RANDOM_NUMBER
    RANDOM_NUMBER = randint(0, 9)
    print(RANDOM_NUMBER)
    return '<main style="text-align: center; margin-top: 30px"><h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" /></main>'

@app.route("/<int:guess>")
def user_guess(guess):

    if guess < RANDOM_NUMBER:
        result_page = f'<main style="text-align: center; margin-top: 30px"><h1 style="color: red">Too low, try again!</h1>' \
           '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" /></main>'
    elif guess > RANDOM_NUMBER:
        result_page = f'<main style="text-align: center; margin-top: 30px"><h1 style="color: purple">Too high, try again!</h1>' \
           '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" /></main>'
    else:
        result_page = f'<main style="text-align: center; margin-top: 30px"><h1 style="color: green">You found me!</h1>' \
           '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" /></main>'
        
    return result_page

if __name__ == '__main__':
    app.run(debug=True)