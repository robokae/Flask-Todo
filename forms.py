from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', 
                                validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', 
                                validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', 
                        validators=[DataRequired(), EqualTo(password)])
    submit = SubmitField('Register')