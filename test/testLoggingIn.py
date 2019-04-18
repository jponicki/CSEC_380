import requests

#you good boo?
def test_login_good_input():
    params = {'username':'new', 'password':'new', 'recap':'L33THAx0rTest'}
    page = requests.get('https://localhost/python/SignIn.py', params=params, verify=False)
    page.encoding = 'utf-8'
    assert 'You are a failure.' not in page.text

#no account, no money bitch
def test_login_noAccount():
    params = {'username':'bitch', 'password':'ass', 'recap':'L33THAx0rTest'}
    page = requests.get('https://localhost/python/SignIn.py', params=params, verify=False)
    page.encoding = 'utf-8'
    assert 'You are a failure.' in page.text

#capturing a moment
def test_login_bad_captcha():
    params = {'username':'new', 'password':'new', 'recap':'xdddd'}
    page = requests.get('https://localhost/python/SignIn.py', params=params, verify=False)
    page.encoding = 'utf-8'
    assert 'Recaptcha Failed. Your parents are not mad, just disappointed.' in page.text
