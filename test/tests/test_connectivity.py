import requests


def test_google():
    r = requests.get("http://www.google.com")
    assert(r.status_code == 200)
