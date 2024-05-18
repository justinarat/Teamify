"""Defines all data routes that the server responds to"""

from flask import request, make_response, jsonify
from app import app, db
from app.model import Lobby, LobbyPlayers, LobbyTags, LobbyTimes, Games


@app.route("/get-lobby-cards", methods=["GET"])
def get_lobby_cards():
    """Endpoint for getting lobby cards for the lobby searching page

    This endpoint takes a GET request with the query string format:
        ?count=<count>
        &search_string=<search_string>
        &search_tags=<tag1>&search_tags=<tag2>...
        &ignore_tags=<tag1>&ignore_tags=<tag2>...

    The body of the response will also have json as:
    body = {
        "lobby_cards"=[
        {
            "lobby_id" : "1",
            "game_title": "game1_title",
            "lobby_name": "lobby1_name",
            "lobby_descrition": "lobby1_desc",
            "host": "host1",
            "players": ["player_1", "player_2", ...],
            "next_available_time": "timeblock format...",
        },
        {
            "lobby_id" : "2",
            "game_title": "game2_title",
            "lobby_name": "lobby2_name",
            "lobby_descrition": "lobby2_desc",
            "host": "host2",
            "players": ["player_a", "player_b", ...],
            "next_available_time": "timeblock format...",
        },
        ...
        ]
    }
    """

    if "count" not in request.args:
        return make_response("Parameter 'count' is missing", 400)

    count = request.args.get("count")

    try:
        count = int(count)
    except ValueError:
        return make_response("Parameter 'count' must be an integer", 400)

    if count < 0:
        return make_response("Parameter 'count' must be greater than or equal to 0", 400)

    if "search_string" not in request.args:
        return make_response("Parameter 'search_string' is missing", 400)

    search_string = request.args.get("search_string")
    search_tags = request.args.getlist("search_tags")

    lobbies = search_db(count, search_string, search_tags)

    lobby_cards = []
    for lobby in lobbies:
        player_usernames = [player.Username for player in lobby.players]
        next_available_time = "" # TODO
        lobby_card = {
            "lobby_id": lobby.LobbyID,
            "game_title": lobby.game.Name,
            "lobby_name": "Lobby Name", # TODO: Change to lobby.Name when that's been merged
            "lobby_description": lobby.Desc,
            "host": lobby.get_host().Username,
            "players": player_usernames,
            "next_available_time": next_available_time,
        }
        lobby_cards.append(lobby_card)

    return jsonify({"lobby_cards": lobby_cards})

def search_db(count, search_string, search_tags):
    """Returns 'count' lobby IDs based on search params"""
    # Filter by tags
    lobby_query = Lobby.query
    for tag in search_tags:
        lobby_query = lobby_query.filter(Lobby.tags.has(Name=tag))

    # Check if search_string is in the lobby game name
    lobby_query = lobby_query.join(Lobby.game).filter(Games.Name.contains(search_string))

    return lobby_query.limit(count).all()
