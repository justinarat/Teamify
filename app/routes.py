from app import app, db
from app.model import Lobby, LobbyPlayers
from app.forms import SignUpForm, LoginForm, CreateLobbyForm
from flask import render_template, redirect, url_for, session, request, flash,jsonify
from app.model import Users, Games
from flask_login import current_user, login_required
from wtforms.validators import DataRequired

@app.route("/")
@app.route("/introduction")
def introduction():
  return render_template("introduction.html", template_folder="templates")

@app.route("/lobby-searching")
def lobby_searching():
  return render_template("lobby-searching.html")

@app.route("/lobby-making", methods=["GET", "POST"])
def lobby_making():
  game_titles = [game[0] for game in Games.query.values(Games.Name)]
  game_titles = game_titles[1:]
  game_titles.sort()
  lobby_making_form = CreateLobbyForm(game_titles=game_titles)
  return render_template("lobby-making.html", title="Create Lobby", lobby_making_form=lobby_making_form)

@app.route("/lobby", methods=["GET"])
@login_required
def lobby_view():
    """Responds with the lobby view page
    
        This expects a query string with a "lobby_id" key which holds the 
        code of the lobby that the user wants to join.
    """
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
    uid = current_user.get_id()
    if uid is not None:  # Ensure uid is not None
        # Debug print to verify uid
        print(f"Current user ID: {uid}")
        lobby_ids = LobbyPlayers.get_lobby_ids_by_user(uid)
        return render_template('my-lobbies.html', lobby_ids=lobby_ids)
    else:
        return "User not logged in", 403



#CODE HERE
def get_max_players(lobby_id):
    lobby = Lobby.query.filter_by(LobbyID=lobby_id).first()
    if lobby:
        return lobby.maxPlayers
    else:
        return None

@app.route('/get_max_players/<int:lobby_id>', methods=['GET'])
def get_max_players_route(lobby_id):
    max_players = get_max_players(lobby_id)
    if max_players is not None:
        return jsonify({'max_players': max_players}), 200
    else:
        return jsonify({'error': 'Lobby not found'}), 404
