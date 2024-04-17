from selenium import webdriver
from selenium.webdriver.remote.command import Command

def test_route(driver, route):
   response = driver.command_executor.execute(Command.GET, {"url": f"http://localhost:5000{route}"})
   print(response)

   # if response == 0:
   #    print(f"Accessed '{route}'")
   # else:
   #    print(f"Could not access '{route}'")

   driver.quit()

if __name__ == "__main__":
   test_route(webdriver.Chrome(), "/")
