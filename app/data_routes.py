from app import app
from flask import request, jsonify, make_response

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
    if not "count" in request.args: 
        return make_response("", 400)
    count = request.args.get("count")
    search_tags = request.args.getlist("search_tags")
    ignore_tags = request.args.getlist("ignore_tags")
    data_to_send = {"lobby_cards": []}
    # TODO: query the database for "count" number of lobby data and put them in data_to_send["lobby_cards"]
    #       Can't do this yet as databases haven't been setup yet in flask
    return jsonify(data_to_send)
