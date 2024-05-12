from app import app, db
from app.model import Lobby, LobbyPlayers
from flask import render_template, redirect, url_for, session, request, flash
from app.forms import SignUpForm, LoginForm
from app.model import Users
from flask_login import current_user, login_required

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

@app.route("/lobby", methods=["GET", "POST"])
@login_required
def lobby_view():
    """Responds with the lobby view page
    
        This expects a query string with a "lobby_id" key which holds the 
        code of the lobby that the user wants to join.
    """
    # Check if the lobby and lobby id exist
    lobby_id = request.args.get("lobby_id")
    lobby = Lobby.query.filter_by(LobbyID=lobby_id).first()
    if lobby_id == None or lobby == None:
        flash("Lobby not found")
        return redirect(url_for("lobby_searching"))

    # If the player is already in the lobby, render full lobby
    lobby_players = LobbyPlayers.query.filter_by(LobbyID=lobby_id)
    user_in_lobby = lobby_players.filter_by(UserID=current_user.get_id()).first() 
    if user_in_lobby:
        session["lobby_id"] = lobby_id
        return render_template("lobby-view.html", template_folder="templates", 
                lobby=lobby, user_in_lobby=user_in_lobby)

    # Check if the lobby is full
    if lobby.is_full():
        flash("Lobby is full, can't join.")
        return redirect(url_for("lobby_searching"))

    return render_template("lobby-view.html", template_folder="templates", 
            lobby=lobby, user_in_lobby=None)

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
