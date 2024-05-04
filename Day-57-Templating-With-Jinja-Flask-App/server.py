from flask import Flask, render_template, url_for
import random
from datetime import datetime
import requests

# Constants.
GENDER_API_ENDPOINT = 'https://api.genderize.io?name='
AGE_API_ENDPOINT = 'https://api.agify.io?name='
BLOG_ENDPOINT = 'https://api.npoint.io/c790b4d5cab58020d391'

# Get the API data.
def get_api(url):
    result = requests.get(url)
    result.raise_for_status()
    data = result.json()
    return data

# Create the flask app.
app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year 
    return render_template('index.html', num = random_number, 
                           year = current_year, name = 'DEBADITYA', 
                           blog_url = url_for('get_blog', post_id=3))


@app.route('/guess/<name>')
def guess_page(name):
    gender_data = get_api(url=f'{GENDER_API_ENDPOINT}{name}')
    age_data = get_api(url=f'{AGE_API_ENDPOINT}{name}')
    return render_template('guess.html', name = name.title(), 
                           gender = gender_data['gender'], age = age_data['age'])

@app.route('/blog/<post_id>')
def get_blog(post_id):
    print(post_id)
    all_posts = get_api(url=BLOG_ENDPOINT)
    return render_template('blog.html', posts = all_posts)

if __name__ == '__main__':
    app.run(debug=True)
