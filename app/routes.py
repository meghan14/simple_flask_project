from flask import render_template
from app import app
from app.game import GamePanel

@app.route("/")
@app.route("/index")
def index():
    user = {"username" : "meghan"}
    posts = [{"quote" :"What a beautiful day"},{"quote": "We have a great weather today!"}]
    return render_template('index.html',title='Home',user=user,posts=posts)

@app.route("/game", methods=['GET','POST'])
def game():
    panel = GamePanel()
    user = {"username": "meghan"}
    return render_template('game.html',title='Game', user=user,form=panel)