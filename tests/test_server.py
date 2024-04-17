import requests

def is_server_running(url: str):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
    except requests.ConnectionError:
        print(f"A connection error occured", end="")
    except requests.Timeout:
        print(f"Request timed out", end="")
    except requests.TooManyRedirects:
        print(f"Request exceeded the maximum number of redirections")
        
    print(f" when attempting to connect to '{url}'.")
    return False

def test_server():
    url = "http://localhost:5000"

    if is_server_running(url):
        print(f"{url} is running.")
    else:
        print(f"{url} is not running.")

if __name__ == "__main__":
    test_server()
