from app import db
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
    print("Emptying database...\n")
    db.session.query(Games).delete()
    db.session.query(Tags).delete()
    db.session.query(Users).delete()
    db.session.query(UserTracker).delete()
    db.session.query(Lobby).delete()
    db.session.query(LobbyPlayers).delete()
    db.session.query(LobbyTags).delete()
    db.session.query(LobbyTimes).delete()


def seed_games():
    data = []

    with open("app/database/games.txt", "r", encoding="utf-8") as file:
        for i, line in enumerate(file):
            data.append(Games(UID=i + 1, Name=line.strip()))

    seed_table("Games", data)


def seed_tags():
    data = [
        Tags(TagID="1", Name="Tag1"),
        Tags(TagID="2", Name="Tag2"),
    ]

    seed_table("Tags", data)


def seed_users(only_required=True):
    data = []
    data.append(
        Users(
            UID="1",
            Username="Admin",
            Password="admin",
            Email="admin@admin.com",
            IsAdmin=1,
        )
    )

    if not only_required:
        data.append(
            Users(
                UID="2",
                Username="CoffeeLover",
                Password="password2",
                Email="coffeelover@gmail.com",
            )
        )
        data.append(
            Users(
                UID="3",
                Username="Firebird",
                Password="password3",
                Email="firebird@outlook.com",
            )
        )

    seed_table("Users", data)


def seed_user_tracker():
    data = [
        UserTracker(
            Time="10/5/2024 12:11:59",
            UserID="1",
            Action="Joined",
            Desc="User1 joined the lobby",
        ),
        UserTracker(
            Time="10/5/2024 17:30:24",
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
    print(f"Seeding {table}...")
    db.session.add_all(data)


def seed_required():
    # Seed required data
    seed_games()
    seed_users(only_required=True)

    # Commit all changes
    db.session.commit()

    print("\nDatabase committed with required seed data successfully!")


def seed_all():
    # Seed all data
    seed_games()
    seed_tags()
    seed_users(only_required=False)
    seed_lobbies()
    seed_lobby_players()
    seed_lobby_times()
    seed_user_tracker()

    # Commit all changes
    db.session.commit()

    print("\nDatabase committed with all seed data successfully!")
