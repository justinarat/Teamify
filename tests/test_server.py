import requests


def can_get_url(url: str):
    try:
        requests.get(url)
        return True
    except requests.RequestException as e:
        return False


def test_get_server():
    server_url = "http://localhost:5000"

    if can_get_url(server_url):
        print(f"Got {server_url}")
    else:
        print(f"Could not get {server_url}")


if __name__ == "__main__":
    test_get_server()
