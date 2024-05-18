from typing import List
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.orm import Mapped

    
class Games(db.Model):
    __tablename__ = 'Games' 
    UID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
    Name = db.Column(db.Text(), nullable=False)


class Tags(db.Model):
    __tablename__ = 'Tags' 
    TagID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
    Name = db.Column(db.Text(), nullable=False)


class Users(UserMixin, db.Model):
    __tablename__ = 'Users' 
    UID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
    Username = db.Column(db.Text(), nullable=False)
    Password = db.Column(db.Text(), nullable=False)
    Email = db.Column(db.Text(), unique=True, nullable=False)

    def set_password(self, password):
        self.Password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.Password, password)
    
    def get_id(self):
        return self.UID

@login.user_loader
def load_student(user_id):
    return Users.query.get(user_id)


class Lobby(db.Model):
    __tablename__ = 'Lobby' 
    LobbyID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
    GameID = db.Column(db.Text(), db.ForeignKey("Games.UID"), nullable=False)
    Desc = db.Column(db.Text())
    game = db.relationship('Games', backref='games', lazy=True)
    players: Mapped[List[Users]] = db.relationship(secondary='LobbyPlayers', backref='lobbyPlayers', lazy=True)
    tags: Mapped[List[Tags]] = db.relationship(secondary='LobbyTags', backref='lobbyPlayers', lazy=True)

    def get_curr_player_count(self):
        return len(self.players)

    def get_max_player_count(self):
        # Creating this for now since max player count column isn't set up yet
        # TODO
        return 3

    def is_full(self):
        return self.get_curr_player_count() >= self.get_max_player_count()

    def get_host(self): # There's probably be a better way of doing this
        host_rel = LobbyPlayers.query.filter_by(LobbyID=self.LobbyID, Authority="host").first()
        if host_rel == None:
            return Users.query.filter_by(UID=0).first()
        return Users.query.filter_by(UID=host_rel.UserID).first()


class LobbyPlayers(db.Model):
    __tablename__ = 'LobbyPlayers' 
    RowID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
    LobbyID = db.Column(db.Text(), db.ForeignKey("Lobby.LobbyID"), nullable=False)
    UserID = db.Column(db.Text(), db.ForeignKey("Users.UID"), nullable=False)
    Authority = db.Column(db.Text(), nullable=False)

    def is_host(self) -> bool:
        return self.Authority == "host"


class LobbyTags(db.Model):
    __tablename__ = 'LobbyTags' 
    RowID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
    LobbyID = db.Column(db.Text(), db.ForeignKey("Lobby.LobbyID"), nullable=False)
    TagID = db.Column(db.Text(), db.ForeignKey("Tags.TagID"), nullable=False)


class LobbyTimes(db.Model):
    __tablename__ = 'LobbyTimes' 
    RowID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
    LobbyID = db.Column(db.Text(), db.ForeignKey("Lobby.LobbyID"), nullable=False)
    TimeBlockStart = db.Column(db.Text(), nullable=False)
    Repeat = db.Column(db.Text(), unique=True, nullable=False)
    TimeBlockEnd = db.Column(db.Text(), nullable=False)
    lobbyRel = db.relationship('Lobby', backref='lobby1', lazy=True)
