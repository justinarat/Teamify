import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app, db
from app.model import (
    Games,
    Tags,
    Users,
    Lobby,
    LobbyPlayers,
    LobbyTags,
    LobbyTimes,
    UserTracker,
)


def empty_db():
    db.session.query(Games).delete()
    db.session.query(Tags).delete()
    db.session.query(Users).delete()
    db.session.query(UserTracker).delete()
    db.session.query(Lobby).delete()
    db.session.query(LobbyPlayers).delete()
    db.session.query(LobbyTags).delete()
    db.session.query(LobbyTimes).delete()
    print("Database emptied successfully!")


def seed_games():
    games = [
        Games(UID="1", Name="Game1"),
        Games(UID="2", Name="Game2"),
    ]

    db.session.add_all(games)


def seed_tags():
    tags = [
        Tags(TagID="1", Name="Tag1"),
        Tags(TagID="2", Name="Tag2"),
    ]

    db.session.add_all(tags)


def seed_users():
    users = [
        Users(
            UID="1", Username="User1", Password="password1", Email="user1@example.com"
        ),
        Users(
            UID="2", Username="User2", Password="password2", Email="user2@example.com"
        ),
    ]

    db.session.add_all(users)


def seed_user_tracker():
    user_tracker = [
        UserTracker(
            RowID="1",
            LobbyID="1",
            UserID="1",
            Action="Joined",
            Desc="User1 joined the lobby",
        ),
        UserTracker(
            RowID="2",
            LobbyID="2",
            UserID="2",
            Action="Joined",
            Desc="User2 joined the lobby",
        ),
    ]

    db.session.add_all(user_tracker)


def seed_lobbies():
    lobbies = [
        Lobby(LobbyID="1", GameID="1", Desc="Lobby1", Name="First Lobby"),
        Lobby(LobbyID="2", GameID="2", Desc="Lobby2", Name="Second Lobby"),
    ]

    db.session.add_all(lobbies)


def seed_lobby_players():
    lobby_players = [
        LobbyPlayers(RowID="1", LobbyID="1", UserID="1", IsHost=1),
        LobbyPlayers(RowID="2", LobbyID="2", UserID="2", IsHost=0),
    ]

    db.session.add_all(lobby_players)


def seed_lobby_times():
    lobby_times = [
        LobbyTimes(
            RowID="1",
            LobbyID="1",
            TimeBlockStart="08:00",
            DayOfWeek="0",
            TimeBlockEnd="10:00",
        ),
        LobbyTimes(
            RowID="2",
            LobbyID="2",
            TimeBlockStart="09:00",
            DayOfWeek="1",
            TimeBlockEnd="11:00",
        ),
    ]

    db.session.add_all(lobby_times)


def seed_required():
    seed_games()
    # TODO: Seed Admin

    print("Database seeded with required data!")


def seed_all():
    # Empty the database
    empty_db()

    # Seed all data
    seed_games()
    seed_tags()
    seed_users()
    seed_lobbies()
    seed_lobby_players()
    # TODO: Seed lobby_tags
    seed_lobby_times()
    seed_user_tracker()

    # Commit all changes
    db.session.commit()

    print("Database seeded with all data!")


if __name__ == "__main__":
    with app.app_context():
        seed_all()
