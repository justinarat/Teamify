from app.blueprints import main
from flask import render_template

@main.route("/")
@main.route("/introduction")
def introduction():
  return render_template("introduction.html", template_folder="templates")

@main.route("/games")
def games_view():
  return render_template("games.html")

@main.route("/lobby-searching")
def lobby_searching():
  return render_template("lobby-searching.html")

@main.route("/lobby-making")
def lobby_making():
  return render_template("lobby-making.html")

@main.route("/lobby")
def lobby_view():
  # TODO: Render the right lobby using the lobby code
  return render_template("lobby-view.html")

@main.route("/account-creation")
def account_creation():
  return render_template("account-creation.html")

@main.route("/admin")
def admin():
  # TODO: maybe use session information (or other way) to verify the user is an admin
  return render_template("admin.html")

@main.route("/my-lobbies")
def my_lobbies():
  # TODO: Render lobbies user belongs to
  # TODO: Render lobbies user owns with choice to view them from user view or admin view
  return render_template("my-lobbies.html")
