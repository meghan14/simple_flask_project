from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class GamePanel(FlaskForm):
    number = IntegerField(" Enter Number ", validators = [DataRequired()])
    submit = SubmitField("Verify!")


