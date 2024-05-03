from flask_tf import FlaskForm
from wtfroms import EmailField, PasswordField, StringField, SubmitField
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
