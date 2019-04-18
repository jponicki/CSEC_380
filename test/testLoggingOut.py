import requests

#bye bye succas
def test_logout():
	params = {'username':'new', 'password':'new', 'recap':'L33THAx0rTest'}
	page = requests.get('https://localhost/python/SignIn.py', params=params, verify=False)
	page.encoding = 'utf-8'
	cookiename = page.text.strip().split(';')[0].split('=')[0]
	cookievalue = page.text.strip().split(';')[0].split('=')[1]
	cookies = {cookiename: cookievalue}
	page = requests.get('https://localhost/python/LoggingOut.py', cookies=cookies, verify=False)
	page.encoding = 'utf-8'
	cookiename = page.text.strip().split(';')[0].split('=')[0]
	cookievalue = page.text.strip().split(';')[0].split('=')[1]
	cookies = {cookiename: cookievalue}
	page = requests.get('https://localhost', cookies=cookies, verify=False)
	assert 'Welcome, come hither.' in page.text
