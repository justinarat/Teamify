"""Tests all data routes present in data_routes.py"""

import unittest
from app import app, db
from app.model import Lobby


class TestGetLobbyCards(unittest.TestCase):
    """
    Tests the get-lobby-cards data route
    """

    def setUp(self):
        host = "localhost"
        port = 5000
        self.url = f"http://{host}:{port}/get-lobby-cards"

        # Add test client and app context
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_cards_no_param(self):
        """Status 400 and empty response returned if GET request has no params"""
        response = self.app.get(self.url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.text, "Parameter 'count' is missing")

    def test_cards_not_int(self):
        """Status 400 and empty response returned if GET request has non-int count"""
        response = self.app.get(self.url, query_string={"count": "fifty"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.text, "Parameter 'count' must be an integer")

    def test_cards_count(self):
        """Number of lobby cards returned matches number requested"""
        test_counts = [0, 1, 5, 25, 125]

        for count in test_counts:
            with self.subTest(count=count):
                response = self.app.get(self.url, query_string={"count": count})

                if count == 0:
                    self.assertEqual(response.status_code, 400)
                    self.assertEqual(
                        response.text, "Parameter 'count' must be greater than 0"
                    )
                else:
                    self.assertEqual(response.status_code, 200)
                    lobby_cards = response.get_json()["lobby_cards"]
                    self.assertEqual(len(lobby_cards), count)

    def test_cards_data_format(self):
        """Response data has correct lobby card keys and values"""
        response = self.app.get(self.url, query_string={"count": 1})
        lobby_cards = response.get_json()["lobby_cards"]

        for card in lobby_cards:
            self.assertEqual(response.status_code, 200)
            self.assertIn("lobby_id", card)
            self.assertIn("game_title", card)
            self.assertIn("lobby_name", card)
            self.assertIn("lobby_description", card)
            self.assertIn("host", card)
            self.assertIn("players", card)
            self.assertIn("next_available_time", card)

    def test_cards_in_database(self):
        """Response data has lobby IDs that are in the database"""
        response = self.app.get(self.url, query_string={"count": 10})
        lobby_cards = response.get_json()["lobby_cards"]

        for card in lobby_cards:
            result = db.session.query(Lobby).filter_by(LobbyID=card["lobby_id"]).first()
            self.assertIsNotNone(result)
