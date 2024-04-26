import unittest
import requests
import sys

def make_request(url, method, **kwargs):
  """Makes an HTTP request to url and return a response object
  Args:
    url (str): the url to send the request to
    method (str): the HTTP method to be used

  Keyword Args:
    query_string (str): query string for a GET request
    data (dict): dictionary to put into the body of a POST request
  """

  if method == "GET".lower():
    return requests.get(url + "?" + kwargs["query_string"])
  elif method == "POST".lower():
    return requests.post(url, kwargs["data"])
  print("Error: invalid request method", file=sys.stderr)
  sys.exit(1)

class DataRoutesTestCase(unittest.TestCase):
  def setUp(self):
    # Assuming Flask is running
    self.url = "http://127.0.0.1:5000"

  def test_get_lobby_cards(self):
    self._test_cards_no_query_string()
    self._test_cards_count(1)
    self._test_cards_count(32)
    self._test_cards_data_format()
  
  def _test_cards_no_query_string(self):
    url = self.url + "/get-lobby-cards"
    response = make_request(url, "get", query_string="")
    self.assertEqual(response.text, "")

  def _test_cards_count(self, count):
    url = self.url + "/get-lobby-cards"
    response = make_request(url, "get", query_string="count=" + str(count))
    response_dict = response.json()
    if count == 0:
      self.assertEqual(response.text, "")
      return
    self.assertEqual(len(response_dict["lobbies"]), count)

  def _test_cards_data_format(self):
    url = self.url + "/get-lobby-cards"
    response = make_request(url, "get", query_string="count=1")
    response_dict = response.json()
    # TODO: Check if the format of the response was correct (has the correct keys and maybe values)
