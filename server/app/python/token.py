#!/usr/bin/python
# checking to see if tokens are valid
import cgi
import MySQLdb
import jwt
import Cookie
import os
import json
from hashlib import sha256

session = None

if 'HTTP_COOKIE' in os.environ:
	cookie_string=os.environ.get('HTTP_COOKIE')
	c=Cookie.SimpleCookie()
	c.load(cookie_string)
	#dem cookies
	try:
		session=c['session'].value
	except KeyError:
		pass

print('Content-Type: text/html')

if session is None:
	print('\r\n')
	print('invalid token')
else:
	try:
		#sweet sweet crypto
		decoded = jwt.decode(session, 'secret', algorithms=['HS256'])
		print('\r\n')
		print(decoded)
	except KeyError:
		print('\r\n')
		print('invalid token')
