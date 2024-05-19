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


def seed_data():
    games = [
        Games(UID="1", Name="Game1"),
        Games(UID="2", Name="Game2"),
    ]

    tags = [
        Tags(TagID="1", Name="Tag1"),
        Tags(TagID="2", Name="Tag2"),
    ]

    users = [
        Users(
            UID="1", Username="User1", Password="password1", Email="user1@example.com"
        ),
        Users(
            UID="2", Username="User2", Password="password2", Email="user2@example.com"
        ),
    ]

    lobbies = [
        Lobby(LobbyID="1", GameID="1", Desc="Lobby1", Name="First Lobby"),
        Lobby(LobbyID="2", GameID="2", Desc="Lobby2", Name="Second Lobby"),
    ]

    lobby_players = [
        LobbyPlayers(RowID="1", LobbyID="1", UserID="1", IsHost=1),
        LobbyPlayers(RowID="2", LobbyID="2", UserID="2", IsHost=0),
    ]

    lobby_tags = [
        LobbyTags(RowID="1", LobbyID="1", TagID="1"),
        LobbyTags(RowID="2", LobbyID="2", TagID="2"),
    ]

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

    # Add the data to the session and commit
    db.session.add_all(games)
    db.session.add_all(tags)
    db.session.add_all(users)
    db.session.add_all(lobbies)
    db.session.add_all(lobby_players)
    db.session.add_all(lobby_tags)
    db.session.add_all(lobby_times)
    db.session.add_all(user_tracker)

    db.session.commit()

    print("Database seeded successfully!")


if __name__ == "__main__":
    with app.app_context():
        seed_data()
