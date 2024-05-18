from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SubmitField, RadioField, IntegerField
from wtforms.validators import DataRequired

class SignUpForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class CreateLobbyForm(FlaskForm):
    game = StringField("Game", validators=[DataRequired()], render_kw={"placeholder": "Enter Game Title"})
    lobby_name = StringField("Lobby Name", validators=[DataRequired()], render_kw={"placeholder": "Enter Lobby Name"})
    lobby_description = StringField("Lobby Description", validators=[DataRequired()], render_kw={"placeholder": "Enter Lobby Description"})
    capacity = IntegerField("Capacity", validators=[DataRequired()], render_kw={"placeholder": "Enter Max Capacity"})
    hidden_tag_field = StringField()
    #input field value attribute