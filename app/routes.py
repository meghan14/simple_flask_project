from flask import render_template, flash, redirect
from app import app
from app.game import GamePanel, GameLogic

@app.route("/")
@app.route("/index")
def index():
    user = {"username" : "User!"}
    posts = [{"quote" :"What a beautiful day"},{"quote": "We have a great weather today!"}]
    return render_template('index.html',title='Home',user=user,posts=posts)

@app.route("/game", methods=['GET','POST'])
def game():
    form = GamePanel()
    user = {"username": "User!"}
    if form.validate_on_submit():
        flash(f'Number entered {form.number.data}')
        message = form.logic.verify_against_secret_number(form.number.data)
        flash(message)
        # return render_template('game.html',title='Game', user=user,form=panel)
    return render_template('game.html', user=user,form=form)