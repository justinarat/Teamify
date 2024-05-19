from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SubmitField, SelectField, IntegerField, TimeField
from wtforms.validators import DataRequired, Optional
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
    game = StringField("Game Title", validators=[DataRequired()], render_kw={"list": "game-options", "placeholder": "Search Games"})
    game_select = SelectField("Game Title", validators=[Optional()])
    lobby_name = StringField("Lobby Name", validators=[DataRequired()], render_kw={"placeholder": "Enter Lobby Name"})
    lobby_description = StringField("Lobby Description", validators=[DataRequired()], render_kw={"placeholder": "Enter Lobby Description"})
    capacity = IntegerField("Capacity", validators=[DataRequired()], render_kw={"placeholder": "Enter Max Capacity"})
    tag1 = StringField(render_kw={"placeholder": "Enter Tag Name"})
    tag2 = StringField(render_kw={"placeholder": "Enter Tag Name"})
    tag3 = StringField(render_kw={"placeholder": "Enter Tag Name"})
    
    mon_from = TimeField("From:", format='%H:%M', validators=[Optional()]) 
    mon_to = TimeField("To:", format='%H:%M', validators=[Optional()]) 
    
    tue_from = TimeField("From:", format='%H:%M', validators=[Optional()]) 
    tue_to = TimeField("To:", format='%H:%M', validators=[Optional()]) 
    
    wed_from = TimeField("From:", format='%H:%M', validators=[Optional()]) 
    wed_to = TimeField("To:", format='%H:%M', validators=[Optional()]) 
    
    thu_from = TimeField("From:", format='%H:%M', validators=[Optional()]) 
    thu_to = TimeField("To:", format='%H:%M', validators=[Optional()]) 
    
    fri_from = TimeField("From:", format='%H:%M', validators=[Optional()]) 
    fri_to = TimeField("To:", format='%H:%M', validators=[Optional()]) 
    
    sat_from = TimeField("From:", format='%H:%M', validators=[Optional()]) 
    sat_to = TimeField("To:", format='%H:%M', validators=[Optional()]) 
    
    sun_from = TimeField("From:", format='%H:%M', validators=[Optional()]) 
    sun_to = TimeField("To:", format='%H:%M', validators=[Optional()]) 
    
    submit = SubmitField("Create Lobby")
