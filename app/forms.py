from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SubmitField, RadioField
from wtforms.validators import DataRequired

class SignUpForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class JoinLobbyForm(FlaskForm):
    join_radio = RadioField(choices=[("Yes", "Yes"), ("No", "No")], validators=[DataRequired()])
    submit = SubmitField("Login")
