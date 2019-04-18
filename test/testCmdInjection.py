import requests

#Stack Overflow amiright
def test_1_command_injection():
	params = {'username':'new', 'password':'new', 'recap':'L33THAx0rTest'}
	page = requests.get('https://localhost/python/SignIn.py', params=params, verify=False)
	page.encoding = 'utf-8'
	cookiename = page.text.strip().split(';')[0].split('=')[0]
	cookievalue = page.text.strip().split(';')[0].split('=')[1]
	cookies = {cookiename: cookievalue}
	params = {'video':'; echo DOES THIS WORK? HELLO GOD? > /var/www/html/videos/INJECTION'}
	page = requests.get('https://localhost/python/buhbye.py', params=params, cookies=cookies, verify=False)
	page = requests.get('https://localhost/videos/INJECTION', cookies=cookies, verify=False)
	assert 'Hello God? Can you hear me?' in page.text

