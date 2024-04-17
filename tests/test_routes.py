import unittest
import requests


class GetRoutesTestCase(unittest.TestCase):
    def check_routes(self, routes, expected_status):
        domain = "http://localhost:5000"
        for route in routes:
            with self.subTest(route=route):
                url = domain + route
                response = requests.get(url, timeout=10)
                self.assertEqual(
                    response.status_code,
                    expected_status,
                    f"Server responded with {response.status_code} rather than {expected_status} at '{url}'",
                )

    def test_get_ok_routes(self):
        routes = ["/", "/test/route"]
        self.check_routes(routes, 200)

    def test_get_missing_routes(self):
        routes = ["/page/not/found", "/this/does/not/exist"]
        self.check_routes(routes, 404)


if __name__ == "__main__":
    unittest.main()
