import unittest
from selenium import webdriver
from selenium.webdriver.remote.command import Command

class SeleniumTestCase(unittest.TestCase):
   def test_route(self, driver, route):
      response = driver.command_executor.execute(Command.GET, {"url": f"http://localhost:5000{route}"})
      print(response)

      # if response == 0:
      #    print(f"Accessed '{route}'")
      # else:
      #    print(f"Could not access '{route}'")

      driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
