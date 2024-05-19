from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SubmitField, SelectField, IntegerField, TimeField
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
    def __init__(self, *args, **kwargs):
        game_titles = kwargs.pop('game_titles', [])
        super(CreateLobbyForm, self).__init__(*args, **kwargs)
        self.game_select.choices = [(title, title) for title in game_titles]
    game = StringField(validators=[DataRequired()], render_kw={"list": "game-options", "placeholder": "Search Games"})
    game_select = SelectField("Game Title")
    lobby_name = StringField("Lobby Name", validators=[DataRequired()], render_kw={"placeholder": "Enter Lobby Name"})
    lobby_description = StringField("Lobby Description", validators=[DataRequired()], render_kw={"placeholder": "Enter Lobby Description"})
    capacity = IntegerField("Capacity", validators=[DataRequired()], render_kw={"placeholder": "Enter Max Capacity"})
    tag1 = StringField(render_kw={"placeholder": "Enter Tag Name"})
    tag2 = StringField(render_kw={"placeholder": "Enter Tag Name"})
    tag3 = StringField(render_kw={"placeholder": "Enter Tag Name"})
    
    mon_from = TimeField("From:", format='%H:%M') 
    mon_to = TimeField("To:", format='%H:%M') 
    
    tue_from = TimeField("From:", format='%H:%M') 
    tue_to = TimeField("To:", format='%H:%M') 
    
    wed_from = TimeField("From:", format='%H:%M') 
    wed_to = TimeField("To:", format='%H:%M') 
    
    thu_from = TimeField("From:", format='%H:%M') 
    thu_to = TimeField("To:", format='%H:%M') 
    
    fri_from = TimeField("From:", format='%H:%M') 
    fri_to = TimeField("To:", format='%H:%M') 
    
    sat_from = TimeField("From:", format='%H:%M') 
    sat_to = TimeField("To:", format='%H:%M') 
    
    sun_from = TimeField("From:", format='%H:%M') 
    sun_to = TimeField("To:", format='%H:%M') 
    
    submit = SubmitField("Create Lobby")
