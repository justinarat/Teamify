import unittest
import requests
import sys

# TODO: maybe put make_request() in a separate file 
def make_request(url, method, **kwargs):
  """Makes an HTTP request to url and return a response object

  Args:
    url (str): the url to send the request to
    method (str): the HTTP method to be used

  Keyword Args:
    query_string (str): query string for a GET request
    data_json (dict): dictionary to put into the body of a POST request
  """

  if method.upper() == "GET":
    return requests.get(url + "?" + kwargs["query_string"])
  elif method.upper() == "POST":
    return requests.post(url, kwargs["data"])
  print("Error: invalid request method", file=sys.stderr)
  sys.exit(1)

class DataRoutesTestCase(unittest.TestCase):
  def setUp(self):
    self.url = "http://127.0.0.1:5000"

  def test_get_lobby_cards(self):
    """Tests the get_lobby_cards() endpoint in data_routes.py"""
    self._test_cards_no_post_body()
    self._test_cards_count(1)
    self._test_cards_count(30)
    self._test_cards_data_format()
  
  def _test_cards_no_count(self):
    """Tests if status 400 and empty response is returned if POST body is invalid (no count)"""
    url = self.url + "/get-lobby-cards"
    response = make_request(url, "POST", data_json={})
    self.assertEqual(response.status_code, 400)
    self.assertEqual(response.text, "")

  def _test_cards_count(self, count):
    """Tests if the number of lobby cards returned matches the number requested"""
    url = self.url + "/get-lobby-cards"
    data_json = {"count": count}
    response = make_request(url, "POST", data_json=data_json)
    response_dict = response.json()
    self.assertEqual(len(response_dict["lobbies"]), count)

  def _test_cards_data_format(self):
    """Tests if the response data has the right lobby card keys and values"""
    url = self.url + "/get-lobby-cards"
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
