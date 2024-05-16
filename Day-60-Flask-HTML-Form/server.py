from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.post('/login')
def login_post():
    return render_template('login.html', username = request.form['username'],
                           password = request.form['password'])

if __name__ == '__main__':
    app.run(debug=True)