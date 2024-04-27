from typing import List
from app import db


class Games(db.Model):
  UID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
  Name = db.Column(db.Text(), nullable=False)

class Lobby(db.Model):
  LobbyID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
  GameID = db.Column(db.Text(), nullable=False)
  Desc = db.Column(db.Text(), nullable=False)
  LobbyPlayersRel = db.relationship('LobbyPlayers', backref='Lobby', lazy=True)
  LobbyTagsRel = db.relationship('LobbyTags', backref='Lobby', lazy=True)
  LobbbyTimesRel = db.relationship('LobbbyTimes', backref='Lobby', lazy=True)

class LobbyPlayers(db.Model):
  RowID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
  LobbyID = db.Column(db.Text(), db.ForeignKey("Lobby.LobbyID"), nullable=False)
  UserID = db.Column(db.Text(), db.ForeignKey("Users.UID"), nullable=False)
  Authority = db.Column(db.Text(), unique=True, nullable=False)

class LobbyTags(db.Model):
  RowID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
  LobbyID = db.Column(db.Text(), db.ForeignKey("Lobby.LobbyID"), nullable=False)
  TagID = db.Column(db.Text(), nullable=False)

class LobbbyTimes(db.Model):
  RowID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
  LobbyID = db.Column(db.Text(), db.ForeignKey("Lobby.LobbyID"), nullable=False)
  TimeBlockStart = db.Column(db.Text(), nullable=False)
  Repeat = db.Column(db.Text(), unique=True, nullable=False)
  TimeBlockEnd = db.Column(db.Text(), nullable=False)

class Tags(db.Model):
  TagID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
  Name = db.Column(db.Text(), nullable=False)


class Users(db.Model):
  UID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
  Username = db.Column(db.Text(), nullable=False)
  Password = db.Column(db.Text(), nullable=False)
  Email = db.Column(db.Text(), unique=True, nullable=False)