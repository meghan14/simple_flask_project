from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {"username" : "meghan"}
    posts = [{"quote" :"What a beautiful day"},{"quote": "We have a great weather today!"}]
    return render_template('index.html',title='Home',user=user,posts=posts)

