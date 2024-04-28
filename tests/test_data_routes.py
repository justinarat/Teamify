import unittest
import requests


class DataRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.url = "http://localhost:5000/get-lobby-cards"

    def test_cards_no_param(self):
        """Tests if status 400 and empty response is returned if GET request has no params"""
        response = requests.get(self.url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.text, "")

    def test_cards_string_count(self):
        """Tests if status 400 and empty response is returned if GET request has string count param"""
        params = {"count": ""}
        response = requests.get(self.url, params=params)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.text, "")

    def test_cards_count(self):
        """Tests if the number of lobby cards returned matches the number requested"""
        test_counts = [0, 1, 5, 25, 125]

        for count in test_counts:
            with self.subTest(count=count):
                params = {"count": count}
                response = requests.get(self.url, params=params)
                self.assertEqual(response.status_code, 200)
                lobby_cards = response.json()["lobby_cards"]
                self.assertEqual(len(lobby_cards), count)

    def test_cards_data_format(self):
        """Tests if the response data has the right lobby card keys and values"""
        params = {"count": 1}
        response = requests.get(self.url, params=params)
        lobby_cards = response.json()["lobby_cards"]
        self.assertEqual(response.status_code, 200)
        # TODO: Check if the format of the response was correct (has the correct keys and maybe values)
        #       Still need to decide on the format, but will likely have:
        self.assertTrue("lobby_id" in lobby_cards)
        self.assertTrue("game_title" in lobby_cards)
        self.assertTrue("lobby_name" in lobby_cards)
        self.assertTrue("lobby_description" in lobby_cards)
        self.assertTrue("host" in lobby_cards)
        self.assertTrue("players" in lobby_cards)
        self.assertTrue("next_available_time" in lobby_cards)
