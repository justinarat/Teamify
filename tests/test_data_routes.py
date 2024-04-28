import unittest
import requests


class DataRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.domain = "http://localhost:5000"

    def test_get_lobby_cards(self):
        """Tests the get_lobby_cards() endpoint in data_routes.py"""
        self._test_cards_no_post_body()
        self._test_cards_count(1)
        self._test_cards_count(30)
        self._test_cards_data_format()

    # TODO: Complete _test_cards_no_post_body implementation
    def _test_cards_no_post_body(self):
        pass

    def _test_cards_no_count(self):
        """Tests if status 400 and empty response is returned if POST body is invalid (no count)"""
        url = self.domain + "/get-lobby-cards"
        response = requests.post(url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.text, "")

    def _test_cards_count(self, count):
        """Tests if the number of lobby cards returned matches the number requested"""
        url = self.domain + "/get-lobby-cards"
        count_json = {"count": count}
        response = requests.post(url, json=count_json)
        self.assertEqual(response.status_code, 200)
        response_dict = response.json()
        self.assertEqual(len(response_dict["lobbies"]), count)

    def _test_cards_data_format(self):
        """Tests if the response data has the right lobby card keys and values"""
        url = self.domain + "/get-lobby-cards"
        response = make_request(url, "POST", query_string="count=1")
        lobby_card_dict = response.json()["lobby_cards"]
        # TODO: Check if the format of the response was correct (has the correct keys and maybe values)
        #       Still need to decide on the format, but will likely have:
        self.assertTrue("lobby_id" in lobby_card_dict)
        self.assertTrue("game_title" in lobby_card_dict)
        self.assertTrue("lobby_name" in lobby_card_dict)
        self.assertTrue("lobby_description" in lobby_card_dict)
        self.assertTrue("host" in lobby_card_dict)
        self.assertTrue("players" in lobby_card_dict)
        self.assertTrue("next_available_time" in lobby_card_dict)
