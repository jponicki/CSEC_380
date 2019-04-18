    
import requests

def test_1_upload_link():
	params = {'username':'new', 'password':'new', 'recap':'L33THAx0rTest'}
	page = requests.get('https://localhost/python/SignIn.py', params=params, verify=False)
	page.encoding = 'utf-8'
	cookiename = page.text.strip().split(';')[0].split('=')[0]
	cookievalue = page.text.strip().split(';')[0].split('=')[1]
	cookies = {cookiename: cookievalue}
	params = {'fileinlink':'https://www.youtube.com/watch?v=3v7_UQu2les', 'videoname':'SON!', 'filein':' '}
	page = requests.get('https://localhost/python/UpVid.py', params=params, cookies=cookies, verify=False)
	assert 'File downloaded, my son' in page.text

def test_2_delete():
	params = {'username':'new', 'password':'new', 'recap':'L33THAx0rTest'}
	page = requests.get('https://localhost/python/SignIn.py', params=params, verify=False)
	page.encoding = 'utf-8'
	cookiename = page.text.strip().split(';')[0].split('=')[0]
	cookievalue = page.text.strip().split(';')[0].split('=')[1]
	cookies = {cookiename: cookievalue}
	params = {'video':'FUCK'}
	page = requests.get('https://localhost/python/buhbye.py', params=params, cookies=cookies, verify=False)
	assert '/html/MyVids.html' in page.text


def test_3_delete_novideo():
	params = {'username':'new', 'password':'new', 'recap':'L33THAx0rTest'}
	page = requests.get('https://localhost/python/SignIn.py', params=params, verify=False)
	page.encoding = 'utf-8'
	cookiename = page.text.strip().split(';')[0].split('=')[0]
	cookievalue = page.text.strip().split(';')[0].split('=')[1]
	cookies = {cookiename: cookievalue}
	params = {'video':'FAKE'}
	page = requests.get('https://localhost/python/buhbye.py', params=params, cookies=cookies, verify=False)
	assert '/html/MyVids.html' in page.text
