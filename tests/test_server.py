import unittest
import requests


class ServerTestCase(unittest.TestCase):
    def test_get_server(self):
        server_url = "http://localhost:5000"
        response = requests.get(server_url, timeout=10)
        self.assertEqual(response.status_code, 200, f"Server responded with {response.status_code} rather than 200")


if __name__ == "__main__":
    unittest.main()
