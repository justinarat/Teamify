from app import socketio
from flask import session
from flask_socketio import emit, join_room, leave_room
import sys

# TODO:
# - Update database for each event if necessary

# data fields:
# - sender_username (could put into cookie)
# - lobby_code: user for socketio room] (could put into cookie)
# - body: different for each event, could be: tag name, lobby name, description, 
#         time schedule, text message, kicked player name

# Events for players joining or leaving
# Shouldn't need to update the database here to add the new player as it should 
#   have been done when the player joins the server (in the lobby_view endpoint)
@socketio.on("player_join")
def player_join():
    sender_user_id, lobby_id = session["user_id"], session["lobby_id"]
    join_room(lobby_id)
    sender_username = "USERNAME" # TODO: Query database for sender username
    data_to_send = {
        "sender_username": sender_username 
    }
    emit("player_join", data_to_send, to=lobby_id)

@socketio.on("player_leave")
def player_leave():
    sender_user_id, lobby_id = session["user_id"], session["lobby_id"]
    # TODO: remove player from lobby in database
    session.pop("lobby_id")
    sender_username = "USERNAME" # TODO: Query database for sender username
    leave_room(lobby_id)
    data_to_send = {
        "sender_username": sender_username
    }
    emit("player_leave", data_to_send, to=lobby_id)

@socketio.on("player_kick")
def player_kick(data):
    sender_user_id, lobby_id = session["user_id"], session["lobby_id"]
    # TODO: Need to figure out how to kick the player so that they can't just
    #       edit the javascript that disconnects them from the lobby
    emit("player_kick", data, to=lobby_id)


# Events all users can send
@socketio.on("player_text")
def player_text(data):
    sender_user_id, lobby_id = session["user_id"], session["lobby_id"]
    sender_username = "USERNAME" # TODO: Query database for sender username
    text_message = data["body"]
    data_to_send = {
        "sender_username": sender_username, 
        "body": text_message
    }
    emit("player_text", data_to_send, to=lobby_id)


# Events only the host (or lobby mods) can send
@socketio.on("add_tag")
def add_tag(data):
    sender_user_id, lobby_id = session["user_id"], session["lobby_id"]
    if not is_lobby_host(sender_user_id): return
    tag = data["body"]
    data_to_send = {
        "body": tag
    }
    emit("add_tag", data_to_send, to=lobby_id)

@socketio.on("remove_tag")
def remove_tag(data):
    sender_user_id, lobby_id = session["user_id"], session["lobby_id"]
    if not is_lobby_host(sender_user_id): return
    tag = data["body"]
    data_to_send = {
        "body": tag
    }
    emit("remove_tag", data_to_send, to=lobby_id)

@socketio.on("change_lobby_name")
def change_lobby_name(data):
    sender_user_id, lobby_id = session["user_id"], session["lobby_id"]
    if not is_lobby_host(sender_user_id): return
    new_lobby_name = data["body"]
    data_to_send = {
        "body": new_lobby_name
    }
    emit("change_lobby_name", data_to_send, to=lobby_id)

@socketio.on("change_description")
def change_description(data):
    sender_user_id, lobby_id = session["user_id"], session["lobby_id"]
    if not is_lobby_host(sender_user_id): return
    new_description = data["body"]
    data_to_send = {
        "body": new_description
    }
    emit("change_lobby_name", data_to_send, to=lobby_id)

@socketio.on("change_time_schedule")
def change_time_schedule(data):
    sender_user_id, lobby_id = session["user_id"], session["lobby_id"]
    if not is_lobby_host(sender_user_id): return
    new_time_schedule = data["body"]
    data_to_send = {
        "body": new_time_schedule
    }
    emit("change_time_schedule", data_to_send, to=lobby_id)

def is_lobby_host(user_id):
    # TODO
    return True
