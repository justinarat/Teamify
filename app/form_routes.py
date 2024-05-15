from app import app, db
from app.model import Users, LobbyPlayers
from app.forms import LoginForm, SignUpForm
from flask import render_template, url_for, redirect, flash, request
from flask_login import login_user, current_user
from sqlalchemy import desc

@app.route("/login-request", methods=["post"])
def login_request():
    """Handles login form requests"""
    login_form = LoginForm()
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data

        user = Users.query.filter_by(Username=username, Password=password).first()
        if user != None:
            # Authentication successful, redirect to some page
            login_user(user)
            return redirect(url_for("games_view"))
        else:
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
def join_lobby_request():
    """Handles request to join lobby, responds with a redirect
    
        Keys in POST body:
            lobby_id - The id of the lobby the user wants to join

            is_joining - "True" if the user wants to join, "False" otherwise
    """

    lobby_id = request.args.get("lobby_id")
    is_joining = request.args.get("is_joining")

    if False: # TODO: Check if the user can join (e.g. lobby full...)
        flash("Lobby is full")
        return redirect(url_for("lobby_searching"))

    if not is_joining: 
        return redirect(url_for("lobby_searching"))

    new_lobby_player = LobbyPlayers(LobbyID=lobby_id, userID=current_user.UID) # TODO: Make new rowid
    db.session.add(new_lobby_player)
    db.session.commit()
    return redirect(url_for("lobby_view", lobby_id=lobby_id))
