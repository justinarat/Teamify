from app import app, db
from app.model import Lobby, Users, LobbyPlayers
from app.forms import LoginForm, SignUpForm
from flask import render_template, url_for, redirect, flash, request, session
from flask_login import login_user, current_user, login_required
from sqlalchemy import desc
from werkzeug.security import generate_password_hash
import flask_socketio

@app.route("/login-request", methods=["post"])
def login_request():
    """Handles login form requests"""
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data

        user = Users.query.filter_by(Email=email).first()
        if user != None:
            if user.check_password(password):
                # Authentication successful, redirect to some page
                login_user(user)
                return redirect(url_for("games_view"))

        # Authentication failed, redirect back to login page
        flash("Invalid username or password")
        signup_form = SignUpForm({}) # {} is to init signup_form with empty data as for some reason it shares data with login_form
        return render_template("account-creation.html", title="Login or Sign Up", 
                login_form=login_form, signup_form=signup_form)

@app.route("/signup-request", methods=["post"])
def signup_request():
    """Handles signup form requests"""
    signup_form = SignUpForm()
    if signup_form.validate_on_submit():
        username = signup_form.username.data
        password = signup_form.password.data
        email = signup_form.email.data

        user = Users.query.filter_by(Email=email).first()
        if user == None:
            # Email not in system, create new user
            user_with_last_uid=Users.query.order_by(desc(Users.UID)).first()
            new_uid = int(user_with_last_uid.UID)+1 # Gets theoretically new UID
            while Users.query.filter_by(UID=new_uid).first() != None: # Guarantees that new_uid is unique
                new_uid += 1

            user = Users(UID=new_uid, Username=username, Email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()

            login_user(user)

            return redirect(url_for("games_view"))
        else:
            # Authentication failed, redirect back to login page
            flash("Invalid Email")
            login_form = LoginForm({}) # {} is to init signup_form with empty data as for some reason it shares data with login_form
            return render_template("account-creation.html", title="Login or Sign Up", 
                    login_form=login_form, signup_form=signup_form)

@app.route("/join-lobby-request", methods=["post"])
@login_required
def join_lobby_request():
    """Handles request to join lobby, responds with a redirect
    
        Keys in POST body:
            lobby_id - The id of the lobby the user wants to join

            is_joining - True if the user wants to join, False otherwise
    """
    data = request.get_json();
    lobby_id = data.get("lobby_id")
    is_joining = data.get("is_joining")

    if lobby_id == None or is_joining == None:
        return "lobby_id or is_joining not given.", 400

    lobby = Lobby.query.filter_by(LobbyID = lobby_id).first()
    if lobby == None:
        return "lobby id does not exist.", 400

    if lobby.is_full():
        flash("Lobby is full, can't join")
        return redirect(url_for("lobby_searching"))

    if not is_joining: 
        return redirect(url_for("lobby_searching"))

    new_row_id = 1000 # TODO: Need to do something better than this to get a new rowid
    while LobbyPlayers.query.filter_by(RowID=new_row_id).first() != None: # Guarantees that new_uid is unique
        new_row_id += 1

    new_lobby_player = LobbyPlayers( \
        RowID=new_row_id,
        LobbyID=lobby_id, 
        UserID=current_user.UID, 
        Authority="player"
    )
    db.session.add(new_lobby_player)
    db.session.commit()

    session["lobby_id"] = lobby_id

    return redirect(url_for("lobby_view", lobby_id=lobby_id))

@app.route("/leave-lobby-request", methods=["post"])
@login_required
def leave_lobby_request():
    user_id = current_user.get_id()
    lobby_id = session["lobby_id"]

    LobbyPlayers.query.filter_by(UserID=user_id, LobbyID=lobby_id).delete()
    db.session.commit()

    del session["lobby_id"]

    data_to_send = {
        "sender_username": current_user.Username
    }
    flask_socketio.emit("player_leave", data_to_send, to=lobby_id, namespace="/")

    return redirect(url_for("lobby_searching"))
