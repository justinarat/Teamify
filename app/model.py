from typing import List
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.orm import Mapped
from datetime import datetime


class Games(db.Model):
    __tablename__ = "Games"
    UID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
    Name = db.Column(db.Text(), nullable=False)


class Tags(db.Model):
    __tablename__ = "Tags"
    TagID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
    Name = db.Column(db.Text(), nullable=False)
    # TagGroup = db.Column(db.Text())
    # Suggestion = db.Column(db.Integer(), default=0)


class Users(UserMixin, db.Model):
    __tablename__ = "Users"
    UID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
    Username = db.Column(db.Text(), nullable=False)
    Password = db.Column(db.Text(), nullable=False)
    Email = db.Column(db.Text(), unique=True, nullable=False)
    IsAdmin = db.Column(db.Integer(), nullable=False, default=0)

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
    __tablename__ = "Lobby"
    LobbyID = db.Column(
        db.Text(), primary_key=True, unique=True, nullable=False, default="4"
    )
    GameID = db.Column(
        db.Text(), db.ForeignKey("Games.UID", name="fk_lobby_game"), nullable=False
    )
    Desc = db.Column(db.Text())
    Name = db.Column(db.Text())
    game = db.relationship("Games", backref="games", lazy=True)
    maxPlayers = db.Column(db.Integer(), default=4)
    players: Mapped[List[Users]] = db.relationship(
        secondary="LobbyPlayers", backref="lobbyPlayers", lazy=True
    )
    tags: Mapped[List[Tags]] = db.relationship(
        secondary="LobbyTags", backref="lobbyPlayers", lazy=True
    )
    time_blocks = db.relationship("LobbyTimes", backref="lobbytimes", lazy=True)

    def get_curr_player_count(self):
        return len(self.players)

    def get_max_player_count(self):
        return self.maxPlayers

    def is_full(self):
        return self.get_curr_player_count() >= self.get_max_player_count()

    def get_host(self):  # There's probably be a better way of doing this
        host_rel = LobbyPlayers.query.filter_by(LobbyID=self.LobbyID, IsHost=1).first()
        if host_rel == None:
            return Users.query.filter_by(UID=0).first()
        return Users.query.filter_by(UID=host_rel.UserID).first()


class LobbyPlayers(db.Model):
    __tablename__ = "LobbyPlayers"
    RowID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
    LobbyID = db.Column(
        db.Text(),
        db.ForeignKey("Lobby.LobbyID", name="fk_lobby_players_lobby"),
        nullable=False,
    )
    UserID = db.Column(
        db.Text(),
        db.ForeignKey("Users.UID", name="fk_lobby_players_user"),
        nullable=False,
    )
    IsHost = db.Column(db.Integer(), nullable=False, default=0)

    @classmethod
    def get_lobby_ids_by_user(cls, user_id):
        results = db.session.query(cls.LobbyID).filter_by(UserID=user_id).all()
        lbby_ids = [result.LobbyID for result in results]
        return lbby_ids

    def is_host(self) -> bool:
        return self.IsHost == 1


class LobbyTags(db.Model):
    __tablename__ = "LobbyTags"
    RowID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
    LobbyID = db.Column(
        db.Text(),
        db.ForeignKey("Lobby.LobbyID", name="fk_lobby_tags_lobby"),
        nullable=False,
    )
    TagID = db.Column(
        db.Text(), db.ForeignKey("Tags.TagID", name="fk_lobby_tags_tag"), nullable=False
    )


class LobbyTimes(db.Model):
    __tablename__ = "LobbyTimes"
    RowID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
    LobbyID = db.Column(
        db.Text(),
        db.ForeignKey("Lobby.LobbyID", name="fk_lobby_times_lobby"),
        nullable=False,
    )
    TimeBlockStart = db.Column(db.Text(), nullable=False)
    DayOfWeek = db.Column(db.Text(), nullable=False)
    TimeBlockEnd = db.Column(db.Text(), nullable=False)

    def get_day_string(self):
        if self.DayOfWeek == "0":
            return "MON"
        if self.DayOfWeek == "1":
            return "TUE"
        if self.DayOfWeek == "2":
            return "WED"
        if self.DayOfWeek == "3":
            return "THU"
        if self.DayOfWeek == "4":
            return "FRI"
        if self.DayOfWeek == "5":
            return "SAT"
        if self.DayOfWeek == "6":
            return "SUN"
        return "TIME"


class UserTracker(db.Model):
    __tablename__ = 'UserTracker'
    Time = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
    UserID = db.Column(
        db.Text(),
        db.ForeignKey("Users.UID", name="fk_user_tracker_user"),
        nullable=False,
    )
    Action = db.Column(db.Text(), nullable=False)
    Desc = db.Column(db.Text())

    _TIME_FORMAT = "%d/%m/%Y %H:%M:%S"

    @classmethod
    def log_login(cls, user):
        current_time = datetime.now().strftime(cls._TIME_FORMAT)
        action = f"{current_time} - {user.Username} logged in."
        desc = f"user_id = {user.UID}"

        log = cls(
            Time=current_time,
            UserID=user.UID,
            Action=action,           
            Desc=desc           
        )
        
        db.session.add(log)
        db.session.commit()

    @classmethod
    def log_signup(cls, user):
        current_time = datetime.now().strftime(cls._TIME_FORMAT)
        action = f"{current_time} - {user.Username} signed up."
        desc = f"user_id = {user.UID}"

        log = cls(
            Time=current_time,
            UserID=user.UID,
            Action=action,           
            Desc=desc           
        )
        
        db.session.add(log)
        db.session.commit()

    @classmethod
    def log_logout(cls, user):
        current_time = datetime.now().strftime(cls._TIME_FORMAT)
        action = f"{current_time} - {user.Username} logged out."
        desc = f"user_id = {user.UID}"

        log = cls(
            Time=current_time,
            UserID=user.UID,
            Action=action,           
            Desc=desc           
        )
        
        db.session.add(log)
        db.session.commit()

    @classmethod
    def log_join_lobby(cls, user, lobby):
        current_time = datetime.now().strftime(cls._TIME_FORMAT)
        action = f"{current_time} - {user.Username} joined {lobby.Name}."
        desc = f"user_id = {user.UID} | lobby_id = {lobby.LobbyID}"

        log = cls(
            Time=current_time,
            UserID=user.UID,
            Action=action,           
            Desc=desc           
        )
        
        db.session.add(log)
        db.session.commit()

    @classmethod
    def log_leave_lobby(cls, user, lobby):
        current_time = datetime.now().strftime(cls._TIME_FORMAT)
        action = f"{current_time} - {user.Username} left {lobby.Name}."
        desc = f"user_id = {user.UID} | lobby_id = {lobby.LobbyID}"

        log = cls(
            Time=current_time,
            UserID=user.UID,
            Action=action,           
            Desc=desc           
        )
        
        db.session.add(log)
        db.session.commit()

    @classmethod
    def log_make_lobby(cls, user, lobby):
        current_time = datetime.now().strftime(cls._TIME_FORMAT)
        action = f"{current_time} - {user.Username} created {lobby.Name}."
        desc = f"user_id = {user.UID} | lobby_id = {lobby.LobbyID}"

        log = cls(
            Time=current_time,
            UserID=user.UID,
            Action=action,           
            Desc=desc           
        )
        
        db.session.add(log)
        db.session.commit()

