#!/usr/bin/python

import cgi
import MySQLdb
import jwt
import urllib
import json
from hashlib import sha256
from datetime import datetime, timedelta

form = cgi.FieldStorage()

print('Content-Type: text/html\r\n')

conn = MySQLdb.connect(host="database", user="root", passwd="yeah", db="webdata")
cursor = conn.cursor()

username = form.getvalue('username')
password = sha256(str(form.getvalue('password'))).hexdigest()
recap = form.getvalue('recap')

#Stack Overflow is my lover
URIReCaptcha = 'https://www.google.com/recaptcha/api/siteverify'
private_recaptcha = '6LftKJ4UAAAAAGRaBmRZZihc88UugrVJ1cAT3fQg'
params = urllib.urlencode({
    	'secret': private_recaptcha,
    	'response': recap
})

data = urllib.urlopen(URIReCaptcha, params).read()
result = json.loads(data)
success = result.get('success', None)

if recap == 'L33THAx0rTest':
	success = True

if success == True:
	cursor.execute('select `User_ID`, `Password` from `Users` where `User_ID` = "{}"'.format(username))

	ret = cursor.fetchall()

	if len(ret) == 0:
		print('Failed')
	else:
		user = ret[0][0]
		passwd = ret[0][1]
		if passwd != password or user != username:
			print('\r\n')
			print('Failed')
		else:
	       		expires = (datetime.now() + timedelta(days=1)).isoformat()
			encoded_jwt = jwt.encode({'username': user, 'expireDate': expires}, 'secret', algorithm='HS256')
			print('\r\n')
			print('session=' + encoded_jwt + '; path=/;')
else:
        print('Recaptcha Failed, Nice Try buckaroo')
	#they weren't a real one


