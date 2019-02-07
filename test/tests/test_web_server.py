import requests


# Test that the text "Hello World" exists on the webpage.
def test_hello_world():
    r = requests.get("http://localhost")
    term = "Hello World"
    assert term in r.text
