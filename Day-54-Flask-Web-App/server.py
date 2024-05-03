from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def bold_func():
        return f'<strong>{func()}</strong>' 
    return bold_func

def make_emphasis(func):
    def emphasis_func():
        return f'<em>{func()}</em>' 
    return emphasis_func

def make_underline(func):
    def underline_func():
        return f'<u>{func()}</u>' 
    return underline_func

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center; margin: 50px auto; color: blue;"">Hello, World!</h1>' \
           '<p style="text-align: center;"><b>Love</b> is in the air!</p>' \
           '<div style="text-align: center;"><img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbHd0aWVsNzFqcTZva2tiMHAxcWFwajZ6cWs0NzFmY3Q4dDFzbDd6ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l4Ki4biBSwhjyrS48/giphy.gif" width=500 /></div>'


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def say_bye():
    return "Bye! See you again."

@app.route('/greet/<user>')
def greetings(user):
    return f"<h3>Hello, {user}</h3><p>How are you, today?</p>"

@app.route('/<user>/<int:age>')
def user_info(user, age):
    return f"<h3>Hello, {user}. You are {age} years old.</h3>"


if __name__ == '__main__':
    app.run(debug=True)