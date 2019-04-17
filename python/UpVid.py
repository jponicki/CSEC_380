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

fileitem = form['filein']
link = form['fileinlink'].value
videoname = form['videoname'].value

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
		cursor.execute('select * from `User Store` where `User Store`.`UID` = "{}"'.format(decoded.get('username')))
		ret = cursor.fetchall()

		if len(ret) == 0:
			print('bad token')
			exit()
		if datetime.now() > datetime.strptime(decoded.get('expireDate'), '%Y-%m-%dT%H:%M:%S.%f'):
			print('bad token')
			exit()

		if fileitem.filename:
			fn = os.path.basename(fileitem.filename.replace("\\", "/" ))
			open('/var/www/html/videos/'+ decoded.get('username')+ '_' + videoname, 'wb').write(fileitem.file.read())

			cursor.execute('insert into `Video` (`User_ID`, `VideoName`, `VideoLoc`) values ("{}", "{}", "{}")'.format(decoded.get('username'), videoname, '/videos/'+decoded.get('username')+'_'+ videoname))
			conn.commit()

			message = 'The file "' + fn + '" was uploaded! Classic.'

		elif link:
			r = urllib.urlopen(link)
			fn = link[link.rfind('/')+1:]
			open('/var/www/html/videos/'+decoded.get('username') + '_' + videoname,'wb').write(r.read())
			message = 'File downloaded'

			cursor.execute('insert into `Video` (`User_ID`, `VideoName`, `VideoLoc`) values ("{}", "{}", "{}")'.format(decoded.get('username'), videoname, '/videos/'+decoded.get('username')+'_'+ videoname))
			conn.commit()

		else:
			message = 'No file was uploaded. RIP.'

		print('\r\n' + message)
		print('<meta http-equiv="refresh" content="1; URL=\'/html/MyVidPage.html\'" />')
	except KeyError:
		print('\r\n')
		print('bad token')
