"""Defines all data routes that the server responds to"""

from flask import request, make_response, jsonify
from app import app, db
from app.model import Lobby, LobbyPlayers, LobbyTags, LobbyTimes, Games


@app.route("/get-lobby-cards", methods=["GET"])
def get_lobby_cards():
    """Endpoint for getting lobby cards for the lobby searching page

    This endpoint takes a GET request with the query string format:
        ?count=<count>&search_tags=<tag1>&search_tags=<tag2>...&
            ignore_tags=<tag1>&ignore_tags=<tag2>...

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

    lobby_cards = []

    for i in range(count):
        lobby_id = i + 1
        # lobby_query = db.session.query(Lobby).filter_by(LobbyID=lobby_id).first()
        lobby_query = db.session.query(Lobby).first()

        if lobby_query:
            game_query = (
                db.session.query(Games).filter_by(UID=lobby_query.GameID).first()
            )
            players_query = db.session.query(LobbyPlayers).filter_by(LobbyID=lobby_id)
            lobby_card = {
                "lobby_id": lobby_query.LobbyID,
                "game_title": game_query.Name,
                "lobby_name": "Lobby Name",
                "lobby_description": lobby_query.Desc,
                "host": "Host Name",
                "players": players_query.all(),
                "next_available_time": "Time",
            }
            lobby_cards.append(lobby_card)

    # TODO:
    # search_tags = request.args.getlist("search_tags")
    # ignore_tags = request.args.getlist("ignore_tags")

    return jsonify({"lobby_cards": lobby_cards})
