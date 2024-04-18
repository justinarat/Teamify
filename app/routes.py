from app import app
from flask import render_template

# Both endpoints are temporary for testing
@app.route("/")
def hello():
  return "Hello World!"

@app.route("/test/route")
def test():
  return "Testing"

# These endpoints could be in the final ver
@app.route("/")
@app.route("/introduction")
def introduction():
  return render_template("introduction.html")

@app.route("/games")
def games_view():
  return render_template("games.html")

@app.route("/lobby-searching")
def lobby_searching():
  return render_template("lobby-searching.html")

@app.route("/lobby/<lobby_code>")
def lobby_view(lobby_code):
  # TODO: Render the right lobby using the lobby code
  return render_template("lobby-view.html")

@app.route("/account-creation")
def account_creation():
  return render_template("account-creation.html")

@app.route("/admin")
def admin():
  # TODO: maybe use session information (or other way) to verify the user is an admin
  return render_template("admin.html")