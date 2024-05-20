from werkzeug.security import generate_password_hash
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
            Password=generate_password_hash("admin"),
            Email="admin@admin.com",
            IsAdmin=1,
        )
    )

    if not only_required:
        extra_data = [
            Users(
                UID="2",
                Username="CoffeeLover",
                Password=generate_password_hash("password2"),
                Email="coffeelover@gmail.com",
            ),
            Users(
                UID="3",
                Username="Firebird",
                Password=generate_password_hash("password3"),
                Email="firebird@outlook.com",
            ),
            Users(
                UID="4",
                Username="Skywalker",
                Password=generate_password_hash("password4"),
                Email="skywalker@gmail.com",
            ),
            Users(
                UID="5",
                Username="Starlord",
                Password=generate_password_hash("password5"),
                Email="starlord@yahoo.com",
            ),
            Users(
                UID="6",
                Username="Moonlight",
                Password=generate_password_hash("password6"),
                Email="moonlight@outlook.com",
            ),
            Users(
                UID="7",
                Username="NightOwl",
                Password=generate_password_hash("password7"),
                Email="nightowl@gmail.com",
            ),
            Users(
                UID="8",
                Username="Sunshine",
                Password=generate_password_hash("password8"),
                Email="sunshine@gmail.com",
            ),
            Users(
                UID="9",
                Username="Rainfall",
                Password=generate_password_hash("password9"),
                Email="rainfall@outlook.com",
            ),
            Users(
                UID="10",
                Username="Snowflake",
                Password=generate_password_hash("password10"),
                Email="snowflake@gmail.com",
            ),
        ]
        for user in extra_data:
            data.append(user)

    seed_table("Users", data)


def seed_lobbies():
    data = [
        Lobby(
            LobbyID="1",
            GameID="1",
            Name="Chill & Chat",
            Desc="Let's chill with some Tetris and have a chat!",
            maxPlayers=3,
        ),
        Lobby(
            LobbyID="2",
            GameID="2",
            Name="Speedrun Race",
            Desc="Race me in a speedrun",
            maxPlayers=2,
        ),
        Lobby(
            LobbyID="3",
            GameID="3",
            Name="Need Help?",
            Desc="I'll help you get all the stars!",
        ),
        Lobby(
            LobbyID="4",
            GameID="4",
            Name="Secrets",
            Desc="Let's explore some secret spots in this game",
        ),
        Lobby(
            LobbyID="5",
            GameID="8",
            Name="Deathwing",
            Desc="I rly need help with this raid",
        ),
        Lobby(
            LobbyID="6",
            GameID="10",
            Name="Smartfridge Gaming",
            Desc="I got the game running on my smartfridge, check it out!!",
        ),
        Lobby(
            LobbyID="7",
            GameID="5",
            Name="Help I'm Scared",
            Desc="I'm scared of this game, help me get through it!",
        ),
        Lobby(
            LobbyID="8",
            GameID="21",
            Name="4 Player Server",
            Desc="Long-term server, looking for 3 more players",
        ),
        Lobby(
            LobbyID="9",
            GameID="1",
            Name="Reach The Rebirth",
            Desc="Wanna make some attempts to reach the rebirth?",
        ),
        Lobby(
            LobbyID="10",
            GameID="20",
            Name="Multiplayer",
            Desc="Need a partner to do the co-op with!",
        ),
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
        LobbyTimes(
            RowID="3",
            LobbyID="3",
            TimeBlockStart="10:00",
            DayOfWeek="2",
            TimeBlockEnd="12:00",
        ),
        LobbyTimes(
            RowID="4",
            LobbyID="4",
            TimeBlockStart="11:00",
            DayOfWeek="3",
            TimeBlockEnd="13:00",
        ),
        LobbyTimes(
            RowID="5",
            LobbyID="5",
            TimeBlockStart="12:00",
            DayOfWeek="4",
            TimeBlockEnd="14:00",
        ),
        LobbyTimes(
            RowID="6",
            LobbyID="6",
            TimeBlockStart="13:00",
            DayOfWeek="5",
            TimeBlockEnd="15:00",
        ),
        LobbyTimes(
            RowID="7",
            LobbyID="7",
            TimeBlockStart="14:00",
            DayOfWeek="6",
            TimeBlockEnd="16:00",
        ),
        LobbyTimes(
            RowID="8",
            LobbyID="8",
            TimeBlockStart="15:00",
            DayOfWeek="0",
            TimeBlockEnd="17:00",
        ),
        LobbyTimes(
            RowID="9",
            LobbyID="9",
            TimeBlockStart="16:00",
            DayOfWeek="1",
            TimeBlockEnd="18:00",
        ),
        LobbyTimes(
            RowID="10",
            LobbyID="10",
            TimeBlockStart="17:00",
            DayOfWeek="2",
            TimeBlockEnd="19:00",
        ),
        LobbyTimes(
            RowID="11",
            LobbyID="2",
            TimeBlockStart="17:00",
            DayOfWeek="3",
            TimeBlockEnd="19:00",
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

    # Commit all changes
    db.session.commit()

    print("\nDatabase committed with all seed data successfully!")
