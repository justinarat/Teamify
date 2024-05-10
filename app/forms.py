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
    title = StringField("Title", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    capacity = IntegerField("Capacity", validators=[DataRequired()])
    hidden_tag_field = StringField()
    #input field value attribute