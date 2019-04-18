import requests

#test that shit
def test_hello_world():
	page = requests.get('http://localhost:80', verify=False)
	page.encoding = 'utf-8'
	assert 'Sup Bitches' in page.text
