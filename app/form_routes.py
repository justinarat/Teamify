from app import app, db
from app.model import Lobby, Users, LobbyPlayers, Games, Tags, LobbyTags
from app.forms import LoginForm, SignUpForm, CreateLobbyForm
from flask import render_template, url_for, redirect, flash, request, session
from flask_login import login_user, current_user, login_required, logout_user
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

@app.route("/create-lobby-request")
@login_required
def create_lobby_request():
    """Handles lobby making requests
    
        Redirects user to page of lobby they just created
    """
    create_lobby_form = CreateLobbyForm()
    
    if create_lobby_form.validate_on_submit():
        
        lobby_with_last_id = Lobby.query.order_by(desc(Lobby.LobbyID)).first()
        new_lobby_id = int(lobby_with_last_id.LobbyID)+1
        while Lobby.query.filter_by(LobbyID=new_lobby_id).first() != None: # Guarantees that new_lobby_id is unique
            new_lobby_id += 1
            
        game = create_lobby_form.game.data
        gameID = int(Games.query.filter_by(Name=game).first().UID)
        
        lobby_name = create_lobby_form.lobby_name.data
        lobby_description = create_lobby_form.lobby_description.data
        capacity = create_lobby_form.capacity.data
        
        tag1 = create_lobby_form.tag1.data
        tag2 = create_lobby_form.tag2.data
        tag3 = create_lobby_form.tag3.data
        
        tag_data_list = [tag1, tag2, tag3]
        
        for tag_name in tag_data_list:
            tag = Tags.query.filter_by(Name=tag_name).first() #check if tag name already exists
            tagID = 0
            if tag == None:
                tag_with_last_id=Tags.query.order_by(desc(Tags.TagID)).first()
                new_tag_id = int(tag_with_last_id.TagID)+1 # Gets theoretically new tag id
                while Tags.query.filter_by(TagID=new_tag_id).first() != None: # Guarantees that new_tag_id is unique id
                    new_tag_id += 1
                tagId = new_tag_id
                new_tag = Tags(TagID=tagID, Name=tag_name)
                db.session.add(new_tag)
            else:
                tagID = int(tag.TagID)
                
            lobby_tag_with_last_id=LobbyTags.query.order_by(desc(LobbyTags.RowID)).first()
            new_lobby_tag_id = int(lobby_tag_with_last_id.RowID)+1
            while LobbyTags.query.filter_by(RowID=new_lobby_tag_id).first() != None: # Guarantees that new_tag_id is unique id
                new_lobby_tag_id += 1
            lobby_tag = LobbyTags(
                RowID=new_lobby_tag_id,
                LobbyID=new_lobby_id,
                TagID=tagID
            )
            db.session.add(lobby_tag)
            
        
        mon_from = create_lobby_form.mon_from.data
        mon_to = create_lobby_form.mon_to.data
        
        tue_from = create_lobby_form.tue_from.data
        tue_to = create_lobby_form.tue_to.data
        
        wed_from = create_lobby_form.wed_from.data
        wed_to = create_lobby_form.wed_to.data
        
        thu_from = create_lobby_form.thu_from.data
        thu_to = create_lobby_form.thu_to.data
        
        fri_from = create_lobby_form.fri_from.data
        fri_to = create_lobby_form.fri_to.data
        
        sat_from = create_lobby_form.sat_from.data
        sat_to = create_lobby_form.sat_to.data
        
        sun_from = create_lobby_form.sun_from.data
        sun_to = create_lobby_form.sun_to.data
        
        new_lobby = Lobby(
            LobbyID=new_lobby_id, 
            GameID=gameID,
            Desc=lobby_description, 
            Name=lobby_name, 
            maxPlayers=capacity,
            # tags=
            )
        db.session.add(new_lobby)
        
        db.session.commit()
        
    return redirect(url_for("introduction"))

@app.route("/logout-request")
@login_required
def logout_request():
    """Handles request for logging out
    
        Redirects user to the introduction page.
    """
    logout_user()
    return redirect(url_for("introduction"))

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
        flash("Lobby is full, can't join.")
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

    data_to_send = {
        "sender_username": current_user.Username 
    }
    flask_socketio.emit("player_join", data_to_send, to=lobby_id, namespace="/")
    session["lobby_id"] = lobby_id

    return redirect(url_for("lobby_view", lobby_id=lobby_id))

@app.route("/leave-lobby-request", methods=["post"])
@login_required
def leave_lobby_request():
    """Handles request to leave a lobby

        Keys in POST body:
            lobby_id - The id of the lobby the user wants to join
    """
    user_id = current_user.get_id()
    lobby_id = session["lobby_id"]

    LobbyPlayers.query.filter_by(UserID=user_id, LobbyID=lobby_id).delete()
    db.session.commit()

    data_to_send = {
        "sender_username": current_user.Username
    }
    flask_socketio.emit("player_leave", data_to_send, to=lobby_id, namespace="/")

    return redirect(url_for("lobby_searching"))
