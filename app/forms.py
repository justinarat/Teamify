from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SubmitField, IntegerField
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

class CreateLobbyForm(FlaskForm):
    game = StringField("Game", validators=[DataRequired()])
    lobby_name = StringField("Lobby Name", validators=[DataRequired()])
    lobby_description = StringField("Lobby Description", validators=[DataRequired()])
    capacity = IntegerField("Capacity", validators=[DataRequired()])
    hidden_tag_field = StringField()
    #input field value attribute