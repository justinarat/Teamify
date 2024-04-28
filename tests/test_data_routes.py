import unittest
import requests


class DataRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.domain = "http://localhost:5000"

    def test_get_lobby_cards(self):
        """Tests the get_lobby_cards() endpoint in data_routes.py"""
        self._test_cards_no_param()
        self._test_cards_count(1)
        self._test_cards_count(30)
        self._test_cards_data_format()

    # TODO: Complete implementation
    def _test_cards_no_param(self):
        pass

    def _test_cards_incorrect_count(self):
        """Tests if status 400 and empty response is returned if GET request is invalid (no count param)"""
        url = self.domain + "/get-lobby-cards"
        params = {"count": ""}
        response = requests.get(url, params=params)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.text, "")

    def _test_cards_count(self, count):
        """Tests if the number of lobby cards returned matches the number requested"""
        url = self.domain + "/get-lobby-cards"
        params = {"count": 1}
        response = requests.get(url, params=params)
        self.assertEqual(response.status_code, 200)
        response_dict = response.json()
        self.assertEqual(len(response_dict["lobbies"]), count)

    def _test_cards_data_format(self):
        """Tests if the response data has the right lobby card keys and values"""
        url = self.domain + "/get-lobby-cards"
        params = {"count": 1}
        response = requests.get(url, params=params)
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
