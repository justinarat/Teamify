from app import app, db
from app.model import Lobby, Users, LobbyPlayers, Games, Tags, LobbyTags, LobbyTimes, UserTracker
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

                UserTracker.log_login(user)

                return redirect(url_for("games_view"))

        # Authentication failed, redirect back to login page
        flash("Invalid email or password")
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

            UserTracker.log_signup(user)

            return redirect(url_for("games_view"))
        else:
            # Authentication failed, redirect back to login page
            flash("Invalid Email")
            login_form = LoginForm({}) # {} is to init signup_form with empty data as for some reason it shares data with login_form
            return render_template("account-creation.html", title="Login or Sign Up", 
                    login_form=login_form, signup_form=signup_form)

@app.route("/create-lobby-request", methods=["post"])
@login_required
def create_lobby_request():
    """Handles lobby making requests
    
        Redirects user to page of lobby they just created
    """
    game_titles = [game[0] for game in Games.query.values(Games.Name)]
    game_titles = game_titles[1:]
    game_titles.sort()
    
    create_lobby_form = CreateLobbyForm(game_titles=game_titles)
    if create_lobby_form.validate_on_submit():
        new_lobby_id = 1
        lobby_with_last_id = Lobby.query.order_by(desc(Lobby.LobbyID)).first()
        if lobby_with_last_id != None:
            new_lobby_id = int(lobby_with_last_id.LobbyID)+1
            while Lobby.query.filter_by(LobbyID=new_lobby_id).first() != None: # Guarantees that new_lobby_id is unique
                new_lobby_id += 1
            
        game = create_lobby_form.game.data
        gameID = int(Games.query.filter_by(Name=game).first().UID)
        
        lobby_name = create_lobby_form.lobby_name.data
        lobby_description = create_lobby_form.lobby_description.data
        capacity = create_lobby_form.capacity.data
        
        tag_data_list = [
            create_lobby_form.tag1.data,
            create_lobby_form.tag2.data,
            create_lobby_form.tag3.data
            ]
        
        for tag_name in tag_data_list:
            if tag_name is not None:
                tag = Tags.query.filter_by(Name=tag_name).first() #check if tag name already exists
                tagID = 0
                if tag == None:
                    new_tag_id = 1;
                    tag_with_last_id=Tags.query.order_by(desc(Tags.TagID)).first()
                    if tag_with_last_id != None:
                        new_tag_id = int(tag_with_last_id.TagID)+1 # Gets theoretically new tag id
                        while Tags.query.filter_by(TagID=new_tag_id).first() != None: # Guarantees that new_tag_id is unique id
                            new_tag_id += 1
                    tagID = new_tag_id
                    new_tag = Tags(TagID=tagID, Name=tag_name)
                    db.session.add(new_tag)
                else:
                    tagID = int(tag.TagID)
                    
                lobby_tag_with_last_id=LobbyTags.query.order_by(desc(LobbyTags.RowID)).first()
                if lobby_tag_with_last_id is not None:
                    new_lobby_tag_id = int(lobby_tag_with_last_id.RowID)+1
                else:
                    new_lobby_tag_id = 0
                while LobbyTags.query.filter_by(RowID=new_lobby_tag_id).first() != None: # Guarantees that new_tag_id is unique id
                    new_lobby_tag_id += 1
                lobby_tag = LobbyTags(
                    RowID=new_lobby_tag_id,
                    LobbyID=new_lobby_id,
                    TagID=tagID
                )
                db.session.add(lobby_tag)
            
        time_froms = [
            create_lobby_form.mon_from.data,
            create_lobby_form.tue_from.data,
            create_lobby_form.wed_from.data,
            create_lobby_form.thu_from.data,
            create_lobby_form.fri_from.data,
            create_lobby_form.sat_from.data,
            create_lobby_form.sun_from.data
        ]
        
        time_tos = [
            create_lobby_form.mon_to.data,
            create_lobby_form.tue_to.data,
            create_lobby_form.wed_to.data,
            create_lobby_form.thu_to.data,
            create_lobby_form.fri_to.data,
            create_lobby_form.sat_to.data,
            create_lobby_form.sun_to.data
        ]

        for i in range(7):
            time_from = time_froms[i]
            time_to = time_tos[i]
            
            if time_from is not None and time_to is not None:
                new_lobby_time_id = 0
                lobby_time_with_last_id=LobbyTimes.query.order_by(desc(LobbyTimes.RowID)).first()
                if lobby_time_with_last_id != None:
                    new_lobby_time_id = int(lobby_time_with_last_id.RowID)+1
                    while LobbyTimes.query.filter_by(RowID=new_lobby_time_id).first() != None: # Guarantees that new_tag_id is unique id
                        new_lobby_time_id += 1
                    
                new_lobby_time = LobbyTimes(
                    RowID=new_lobby_time_id,
                    LobbyID=new_lobby_id,
                    TimeBlockStart=time_from.strftime("%H:%M"),
                    DayOfWeek=i,
                    TimeBlockEnd=time_to.strftime("%H:%M")
                )
                db.session.add(new_lobby_time)
        
        new_lobby = Lobby(
            LobbyID=new_lobby_id, 
            GameID=gameID,
            Desc=lobby_description, 
            Name=lobby_name, 
            maxPlayers=capacity
        )
        db.session.add(new_lobby)

        new_lobby_players_id = 0
        lobby_player_with_last_id=LobbyPlayers.query.order_by(desc(LobbyPlayers.RowID)).first()
        if lobby_player_with_last_id != None:
            new_lobby_players_id = int(lobby_player_with_last_id.RowID)+1
            while LobbyPlayers.query.filter_by(RowID=new_lobby_players_id).first() != None: # Guarantees that new_tag_id is unique id
                new_lobby_players_id += 1

        new_lobby_player = LobbyPlayers(
            RowID=new_lobby_players_id,
            LobbyID=new_lobby_id,
            UserID=current_user.get_id(),
            IsHost=1
        )
        db.session.add(new_lobby_player)
        
        db.session.commit()
        
        UserTracker.log_make_lobby(current_user, new_lobby)

        return redirect(url_for("lobby_view", lobby_id=new_lobby_id))
    print(create_lobby_form.errors)
    print("Form data:", create_lobby_form.data)
    return "Form validation failed. Please try again.", 400

@app.route("/logout-request")
@login_required
def logout_request():
    """Handles request for logging out
    
        Redirects user to the introduction page.
    """
    UserTracker.log_logout(current_user)

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
        IsHost=0
    )
    db.session.add(new_lobby_player)
    db.session.commit()

    data_to_send = {
        "sender_username": current_user.Username 
    }
    flask_socketio.emit("player_join", data_to_send, to=lobby_id, namespace="/")
    session["lobby_id"] = lobby_id

    UserTracker.log_join_lobby(current_user, lobby)

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

    # Both user_id and lobby_id should exist in LobbyPlayers since the leave button 
    # won't render unless they're in the lobby, so no error checking done

    LobbyPlayers.query.filter_by(UserID=user_id, LobbyID=lobby_id).delete()
    db.session.commit()

    data_to_send = {
        "sender_username": current_user.Username
    }
    flask_socketio.emit("player_leave", data_to_send, to=lobby_id, namespace="/")

    lobby = Lobby.query.filter_by(LobbyID=lobby_id).first()

    UserTracker.log_leave_lobby(current_user, lobby)

    return redirect(url_for("lobby_searching"))
