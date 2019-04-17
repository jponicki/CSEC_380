#!/usr/bin/python

import cgi, os
import cgitb; cgitb.enable()
import MySQLdb
import jwt
import Cookie
import urllib
from os import environ
from datetime import datetime, timedelta
import json

print('Content-type: text/html\r\n')

conn = MySQLdb.connect(host="database", user="root", passwd="yeah", db="webdata")
cursor = conn.cursor()

form = cgi.FieldStorage()

token = None
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

if session is None:
   	print('\r\n')
   	print('bad token')
else:
   	try:
      		print('\r\n')

      		decoded = jwt.decode(session, 'secret', algorithms=['HS256'])
      		cursor.execute('select * from `Users` where `Users`.`User_ID` = "{}"'.format(decoded.get('username')))
      		ret = cursor.fetchall()

      		if len(ret) == 0:
         		print('bad token')
         		exit()

      		if datetime.now() > datetime.strptime(decoded.get('expireDate'), '%Y-%m-%dT%H:%M:%S.%f'):
         		print('bad token')
         		exit()
			#dat bitch old
		
      		expires = (datetime.strptime('1970-1-1T12:34:56.100000','%Y-%m-%dT%H:%M:%S.%f').isoformat())
      		encoded_jwt = jwt.encode({'username': decoded.get('username'), 'expireDate': expires}, 'secret', algorithm='HS256')
      		print('\r\n')
      		print('session=' + encoded_jwt + '; path=/;')

   	except KeyError:
      		print('\r\n')
      		print('bad token')
