from flask import Flask, render_template

app = Flask(__name__)
print(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/<username>")
def hi(username=None):
    return render_template('hi.html', name=username)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/blog")
def blog():
    return "<p>this is a blog page!</p>"


@app.route("/blog/<int:year>/<post_title>")
def blog_post(year=None, post_title=None):
    return render_template('blog.html', year=year, title=post_title)
