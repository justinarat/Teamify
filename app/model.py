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
    #TagGroup = db.Column(db.Text())
    #Suggestion = db.Column(db.Integer(), default=0)


class Users(UserMixin, db.Model):
    __tablename__ = 'Users'
    UID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
    Username = db.Column(db.Text(), nullable=False)
    Password = db.Column(db.Text(), nullable=False)
    Email = db.Column(db.Text(), unique=True, nullable=False)
    IsAdmin = db.Column(db.Integer(), nullable=False,default=0)

    def set_password(self, password):
        self.Password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.Password, password)
    def is_admin(self):
        return self.IsAdmin == 1
    
    def get_id(self):
        return self.UID

    def is_admin(self):
        return self.IsAdmin == 1

@login.user_loader
def load_student(user_id):
    return Users.query.get(user_id)


class Lobby(db.Model):
    __tablename__ = 'Lobby'
    LobbyID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False, default="4")
    GameID = db.Column(db.Text(), db.ForeignKey("Games.UID", name="fk_lobby_game"), nullable=False)
    Desc = db.Column(db.Text())
    Name = db.Column(db.Text())
    game = db.relationship('Games', backref='games', lazy=True)
    maxPlayers = db.Column(db.Integer(), default=4)
    players: Mapped[List[Users]] = db.relationship(secondary='LobbyPlayers', backref='lobbyPlayers', lazy=True)
    tags: Mapped[List[Tags]] = db.relationship(secondary='LobbyTags', backref='lobbyPlayers', lazy=True)

    def get_curr_player_count(self):
        return len(self.players)

    def get_max_player_count(self):
        return self.maxPlayers

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
    LobbyID = db.Column(db.Text(), db.ForeignKey("Lobby.LobbyID", name="fk_lobby_players_lobby"), nullable=False)
    UserID = db.Column(db.Text(), db.ForeignKey("Users.UID", name="fk_lobby_players_user"), nullable=False)
    Authority = db.Column(db.Text(), nullable=False)
    
    @classmethod
    def get_lobby_ids_by_user(cls, user_id):
        results = db.session.query(cls.LobbyID).filter_by(UserID=user_id).all()
        lbby_ids = [result.LobbyID for result in results]
        return lbby_ids

    def is_host(self) -> bool:
        return self.Authority == "host"


class LobbyTags(db.Model):
    __tablename__ = 'LobbyTags'
    RowID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
    LobbyID = db.Column(db.Text(), db.ForeignKey("Lobby.LobbyID", name="fk_lobby_tags_lobby"), nullable=False)
    TagID = db.Column(db.Text(), db.ForeignKey("Tags.TagID", name="fk_lobby_tags_tag"), nullable=False)


class LobbyTimes(db.Model):
    __tablename__ = 'LobbyTimes'
    RowID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
    LobbyID = db.Column(db.Text(), db.ForeignKey("Lobby.LobbyID", name="fk_lobby_times_lobby"), nullable=False)
    TimeBlockStart = db.Column(db.Text(), nullable=False)
    Repeat = db.Column(db.Text(), nullable=False)
    TimeBlockEnd = db.Column(db.Text(), nullable=False)
    lobbyRel = db.relationship('Lobby', backref='lobby1', lazy=True)


class UserTracker(db.Model):
    __tablename__ = 'UserTracker'
    RowID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
    LobbyID = db.Column(db.Text(), db.ForeignKey("Lobby.LobbyID", name="fk_user_tracker_lobby"), nullable=False)
    UserID = db.Column(db.Text(), db.ForeignKey("Users.UID", name="fk_user_tracker_user"), nullable=False)
    Action = db.Column(db.Text(), nullable=False)
    Desc = db.Column(db.Text())
    user2Rel = db.relationship('Users', backref='users2', lazy=True)
    lobby2Rel = db.relationship('Lobby', backref='lobby4', lazy=True)
