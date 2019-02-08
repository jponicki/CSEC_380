import requests


# Check if the HTTP Response was 200
def test_server_accessible():
    r = requests.get("http://localhost")
    assert r.status_code == 200


# Test that the text "Hello World" exists on the webpage.
def test_hello_world():
    r = requests.get("http://localhost")
    term = "Hello World"
    assert term in r.text
