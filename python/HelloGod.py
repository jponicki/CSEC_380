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
      		param = form['search'].value
      		query = 'select `Username`,`VideoName`, `VideoLoc` from `Video` join `Users` where `Users`.`User_ID` = `Video`.`User_ID` and `Video`.`VideoName` = \"'+param+'\"'
      		cursor.execute(query)
      		rows = cursor.fetchall()

      		if len(rows) == 0:
         		print('Sorry there were no results for "{}"'.format(form['search'].value))
      		else:
         		print('<h4>Results</h4>')
         		for row in rows:
             		print("""<video width="320" height="240" poster={} controls>
                  		<source src="{}" type="video/mp4">
                  		<source src="{}" type="video/webm">
                  		Your browser does not support the video tag.
                  		</video></br>""".format(row[2], row[2], row[2]))
             		print('User: {} Title: {}'.format(row[0],row[1]))
             		print('</br>')
			#dats a big RIP

   	except KeyError:
      		print('\r\n')
      		print('bad token')
