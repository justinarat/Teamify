import unittest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class SeleniumTestCase(unittest.TestCase):
    def check_routes_with_driver(self, driver: WebDriver):
        domain = "http://localhost:5000"
        routes = ["/", "/test/route"]
        for route in routes:
            driver.get(domain + route)
        driver.quit()

    def test_routes_with_chrome(self):
        self.check_routes_with_driver(webdriver.Chrome())

    def test_routes_with_firefox(self):
        self.check_routes_with_driver(webdriver.Firefox())

    def test_routes_with_edge(self):
        self.check_routes_with_driver(webdriver.Edge())


if __name__ == "__main__":
    unittest.main(verbosity=2)
