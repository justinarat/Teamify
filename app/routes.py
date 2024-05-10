from app import app, db
from flask import render_template, redirect, url_for, session, request
from app.forms import SignUpForm, LoginForm
from app.model import Users

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
  # - Render the right lobby using the lobby code.
  # - If user hasn't joined the lobby (not joined in database), redirect to 
  #     lobby searching page.
  session["lobby_id"] = request.args.get("lobby_id")
  session["user_id"] = "0000" # TODO: Use FLaskLogin to get user object
  return render_template("lobby-view.html", template_folder="templates")

@app.route("/account-creation", methods=["GET", "POST"])
def account_creation():
  login_form = LoginForm()
  signup_form = SignUpForm()
  return render_template("account-creation.html", title="Login or Sign Up", login_form=login_form, signup_form=signup_form)

@app.route("/admin")
def admin():
  # TODO: maybe use session information (or other way) to verify the user is an admin
  return render_template("admin.html")

@app.route("/my-lobbies")
def my_lobbies():
  # TODO: Render lobbies user belongs to
  # TODO: Render lobbies user owns with choice to view them from user view or admin view
  return render_template("my-lobbies.html")
