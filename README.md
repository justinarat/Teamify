# Teamify

## About the project

the app is meant to allow players who are looking for a group of people to play with to find other players without having to mess with scheduling conflicts or figuring out crossplay or playstyle. using teamify users can create lobbies with tags that allow users to see at a glance what the lobby is looking for in a player and find a group of players that match their playstyle. with lobby chat, players can coordinate setup and joining of a multplayer game, and learn about each other and decide if they want to play together before actually allowing other people into game servers.

## Project Group

| UWA ID   | Name                   | Github         |
|----------|------------------------|----------------|
| 23080798 | Justin Arat            | justinarat     |
| 23431003 | Dominic Davies         | dominictdavies |
| 23395411 | John Giampaolo         | JohnGiampaolo  |
| 22992693 | Fatimah Ali O Aljanobi | FAljanobi      |

## Summary of Application Architecture

```plaintext
app
 database
  main.db(to be genned)
  seed.py(helps in creation and population of db)
 static
  css
   (holds all css files we made)
   base.css(used as base css in all pages)
   introduction.css
   lobby-making.css
   lobby-view.css
  scripts
   (holds all js)
 templates
  (has all html files)
  base.html(used to make the header consistant)
  (all other html are based on a page)
deliverables
migrations
 versions
  (holds all migration code)
 alembic.ini
 env.py
 script.py.mako
 tests
  (hold test scripts)
readme.md(you are here)
requriements.txt(states all project requirements)
```

## Launching the application

1. Create a virtual environment `python3 -m venv .venv`
2. Activate the virtual environment `source .venv/bin/activate`
3. Install project requirements `pip install -r requirements.txt`
4. Set the environment variable (use a different key instead of "poor secret")
    `export CITS3403_FLASK_SECRET_KEY="poor secret"`
    for windows:
    `set CITS3403_FLASK_SECRET_KEY="poor secret"`
5. Start up the flask server `flask run`

## Creating and seeding the database

1. Run `flask db upgrade` to construct the database
2. Run `flask seed` to seed the database with required data

Extra testing data can be seeded instead with `flask seed all`

## Running tests

First, in a separate terminal start up the flask server if it's not running:
`flask run`

To run all tests:
`python -m unittest`

To run specific test modules:
`python -m unittest tests.test_file`
