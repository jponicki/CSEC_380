import requests

#test if new account
def test_newAccount_input():
	params = {'username':'new', 'password':'new', 'displayName':'new', 'recap':'L33THAx0rTest'}
	page = requests.get('https://localhost/python/CreateAccount.py', params=params, verify=False)
	page.encoding = 'utf-8'
	assert 'User Made' in page.text

#test if existing
def test_newAccount_user_exists():
	params = {'username':'new', 'password':'new', 'displayName':'new', 'recap':'L33THAx0rTest'}
	page = requests.get('https://localhost/python/CreateAccount.py', params=params, verify=False)
	page.encoding = 'utf-8'
	assert 'Already an Existing User' in page.text

#test if captcha failed
def test_newAccount_bad_captcha():
	params = {'username':'new', 'password':'new', 'displayName':'new', 'recap':'xdddd'}
	page = requests.get('https://localhost/python/CreateAccount.py', params=params, verify=False)
	page.encoding = 'utf-8'
	assert 'Recaptcha Failed, Succa' in page.text
