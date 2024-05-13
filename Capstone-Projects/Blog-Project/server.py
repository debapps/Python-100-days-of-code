from flask import Flask, render_template
import requests
from post import Post

# Constants
BLOG_URL = 'https://api.npoint.io/6c785bf63668cabee2e2'

def get_blogs():
    # Get the data from API.
    response = requests.get(BLOG_URL)
    response.raise_for_status()
    data = response.json()
    
    # Generate the Post list from API data.
    blogs = []
    for item in data['posts']:
        post = Post(item['id'], item['title'], item['subtitle'], 
                    item['author'], item['body'], item['published-date'], item['img-url'])
        blogs.append(post)
    return blogs

# Create the Flask Application. 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', blogs = get_blogs())

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/blog/<int:postid>")
def blog(postid):
    # Get all blogs
    blogs = get_blogs()

    # Get the blog with postid.
    blog = None
    for post in blogs:
        if post.id == postid:
            blog = post
            break
    
    return render_template("post.html", post = blog)

if __name__ == '__main__':
    app.run(debug=True)