from app import db


class Games(db.Model):
    __tablename__ = 'Games'
    UID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
    Name = db.Column(db.Text(), nullable=False)


class Tags(db.Model):
    __tablename__ = 'Tags'
    TagID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
    Name = db.Column(db.Text(), nullable=False)
    TagGroup = db.Column(db.Text())
    Suggestion = db.Column(db.Integer(), default=0)


class Users(db.Model):
    __tablename__ = 'Users'
    UID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
    Username = db.Column(db.Text(), nullable=False)
    Password = db.Column(db.Text(), nullable=False)
    Email = db.Column(db.Text(), unique=True, nullable=False)


class Lobby(db.Model):
    __tablename__ = 'Lobby'
    LobbyId = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
    GameID = db.Column(db.Text(), db.ForeignKey("Games.UID", name="fk_lobby_game"), nullable=False)
    Desc = db.Column(db.Text())
    gamesRel = db.relationship('Games', backref='games', lazy=True)


class LobbyPlayers(db.Model):
    __tablename__ = 'LobbyPlayers'
    RowID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
    LobbyId = db.Column(db.Text(), db.ForeignKey("Lobby.LobbyId", name="fk_lobby_players_lobby"), nullable=False)
    UserID = db.Column(db.Text(), db.ForeignKey("Users.UID", name="fk_lobby_players_user"), nullable=False)
    Authority = db.Column(db.Text(), nullable=False)
    userRel = db.relationship('Users', backref='users', lazy=True)
    lobbyRel = db.relationship('Lobby', backref='lobby3', lazy=True)


class LobbyTags(db.Model):
    __tablename__ = 'LobbyTags'
    RowID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
    LobbyId = db.Column(db.Text(), db.ForeignKey("Lobby.LobbyId", name="fk_lobby_tags_lobby"), nullable=False)
    TagID = db.Column(db.Text(), db.ForeignKey("Tags.TagID", name="fk_lobby_tags_tag"), nullable=False)
    tagRel = db.relationship('Tags', backref='tags', lazy=True)
    lobbyRel = db.relationship('Lobby', backref='lobby2', lazy=True)


class LobbyTimes(db.Model):
    __tablename__ = 'LobbyTimes'
    RowID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
    LobbyId = db.Column(db.Text(), db.ForeignKey("Lobby.LobbyId", name="fk_lobby_times_lobby"), nullable=False)
    TimeBlockStart = db.Column(db.Text(), nullable=False)
    Repeat = db.Column(db.Text(), unique=True, nullable=False)
    TimeBlockEnd = db.Column(db.Text(), nullable=False)
    lobbyRel = db.relationship('Lobby', backref='lobby1', lazy=True)


class UserTracker(db.Model):
    __tablename__ = 'UserTracker'
    RowID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
    LobbyId = db.Column(db.Text(), db.ForeignKey("Lobby.LobbyId", name="fk_user_tracker_lobby"), nullable=False)
    UserID = db.Column(db.Text(), db.ForeignKey("Users.UID", name="fk_user_tracker_user"), nullable=False)
    Action = db.Column(db.Text(), nullable=False)
    Desc = db.Column(db.Text())
    user2Rel = db.relationship('Users', backref='users2', lazy=True)
    lobby2Rel = db.relationship('Lobby', backref='lobby4', lazy=True)
