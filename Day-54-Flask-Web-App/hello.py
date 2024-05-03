from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/bye")
def say_bye():
    return "<h2>Bye! See you again.</h2>"


if __name__ == '__main__':
    app.run()