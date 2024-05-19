import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app, db
from app.model import (
    Games,
    Tags,
    Users,
    UserTracker,
    Lobby,
    LobbyPlayers,
    LobbyTags,
    LobbyTimes,
)


def empty_db():
    print("Emptying database")
    db.session.query(Games).delete()
    db.session.query(Tags).delete()
    db.session.query(Users).delete()
    db.session.query(UserTracker).delete()
    db.session.query(Lobby).delete()
    db.session.query(LobbyPlayers).delete()
    db.session.query(LobbyTags).delete()
    db.session.query(LobbyTimes).delete()


def seed_games():
    data = [
        Games(UID="1", Name="Game1"),
        Games(UID="2", Name="Game2"),
    ]

    seed_table("Games", data)


def seed_tags():
    data = [
        Tags(TagID="1", Name="Tag1"),
        Tags(TagID="2", Name="Tag2"),
    ]

    seed_table("Tags", data)


def seed_users():
    data = [
        Users(
            UID="1", Username="User1", Password="password1", Email="user1@example.com"
        ),
        Users(
            UID="2", Username="User2", Password="password2", Email="user2@example.com"
        ),
    ]

    seed_table("Users", data)


def seed_user_tracker():
    data = [
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

    seed_table("UserTracker", data)


def seed_lobbies():
    data = [
        Lobby(LobbyID="1", GameID="1", Desc="Lobby1", Name="First Lobby"),
        Lobby(LobbyID="2", GameID="2", Desc="Lobby2", Name="Second Lobby"),
    ]

    seed_table("Lobby", data)


def seed_lobby_players():
    data = [
        LobbyPlayers(RowID="1", LobbyID="1", UserID="1", IsHost=1),
        LobbyPlayers(RowID="2", LobbyID="2", UserID="2", IsHost=0),
    ]

    seed_table("LobbyPlayers", data)


def seed_lobby_times():
    data = [
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

    seed_table("LobbyTimes", data)


def seed_table(table, data):
    print(f"Seeding {table}")
    db.session.add_all(data)


def seed_required():
    # Seed required data
    seed_games()
    # TODO: Seed Admin

    # Commit all changes
    db.session.commit()

    print("Database committed with required seed data successfully!")


def seed_all():
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

    print("Database committed with all seed data successfully!")


if __name__ == "__main__":
    with app.app_context():
        empty_db()
        seed_all()
