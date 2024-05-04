from flask import Flask, render_template, url_for
from post import Post

app = Flask(__name__)

def get_link_posts(posts):
    link_post = []
    for post in posts:
        post['link'] = url_for('blogpost', blogid = post['id'])
        link_post.append(post)
    return link_post

post = Post()

@app.route('/')
def home():
    link_posts = get_link_posts(post.get_all_posts())
    return render_template("index.html", posts = link_posts)

@app.route('/post/<int:blogid>')
def blogpost(blogid):
    blog_post = post.get_post(blogid)
    return render_template('post.html', blog = blog_post)

if __name__ == "__main__":
    app.run()
