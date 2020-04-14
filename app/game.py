from flask_wtf import FlaskForm
import random
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired


class GameLogic(object):
    ALLOWED_ATTEMPTS = 7  # initialize with seven attempts
    def __init__(self, attempts: int = 7, range: int = 100) -> object:
        if attempts < self.ALLOWED_ATTEMPTS:
            self.attempts = attempts
            self.ALLOWED_ATTEMPTS = attempts
        else:
            self.attempts = self.ALLOWED_ATTEMPTS
        self.secret_number = random.randrange(0, range)

    def reset_game(self, range):
        self.attempts = self.ALLOWED_ATTEMPTS
        self.secret_number = random.randrange(0, range)

    def verify_against_secret_number(self,number):
        guessed_number = int(number)
        self.attempts -=1
        if not guessed_number is self.secret_number:
            if guessed_number > self.secret_number:
                message = f'Wrong! Try going lower. Total attempts left: {self.attempts}!!'
            elif guessed_number < self.secret_number:
                message = f'Wrong! Try going higher. Total attempts left: {self.attempts}!!'
            if self.attempts == 0:
                message = f"Hard Luck! You are out of attempts. The secret number was {self.secret_number} " \
                          f" Starting a new Game..."
                self.reset_game(100)
            return message
        else:
            message = f"Great Job! You guessed the no. in  {self.ALLOWED_ATTEMPTS - self.attempts} attempts!! " \
                      f"  Starting a new Game.."
            self.reset_game(100)
        return message

class GamePanel(FlaskForm):
    number = IntegerField(" Enter Number: ", validators=[DataRequired()])
    submit = SubmitField("Verify!")
    logic = GameLogic()
