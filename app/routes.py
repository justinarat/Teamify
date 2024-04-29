from app import app
from flask import render_template

@app.route("/")
@app.route("/introduction")
def introduction():
  return render_template("introduction.html", template_folder="templates")

@app.route("/games")
def games_view():
  return render_template("games.html")

@app.route("/lobby-searching")
def lobby_searching():
  return render_template("lobby-searching.html")

@app.route("/lobby-making")
def lobby_making():
  return render_template("lobby-making.html")

@app.route("/lobby")
def lobby_view():
  # TODO: 
  # - Figure out how the user gets the lobby code in session cookie
  # - Render the right lobby using the lobby code
  # - If user hasn't joined this lobby (has the lobby code in session cookie)
  #     redirect them to lobby searching page
  return render_template("lobby-view.html")

@app.route("/account-creation")
def account_creation():
  return render_template("account-creation.html")

@app.route("/admin")
def admin():
  # TODO: maybe use session information (or other way) to verify the user is an admin
  return render_template("admin.html")

@app.route("/my-lobbies")
def my_lobbies():
  # TODO: Render lobbies user belongs to
  # TODO: Render lobbies user owns with choice to view them from user view or admin view
  return render_template("my-lobbies.html")
