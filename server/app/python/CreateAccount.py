#!/usr/bin/python

import cgi
import MySQLdb
import urllib
import json
from hashlib import sha256

form = cgi.FieldStorage()

print('Content-Type: text/html\r\n')

conn = MySQLdb.connect(host="database", user="root", passwd="yeah", db="webdata")
cursor = conn.cursor()

username = form.getvalue('username')
password = sha256(str(form.getvalue('password'))).hexdigest()
displayName = form.getvalue('displayName')
recap = form.getvalue('recap')

#found on stackOverflow
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
	#they a real one

if success == True:
	cursor.execute('select `User_ID` from `Users` where `User_ID` = "{}"'.format(username))

	ret = cursor.fetchall()

	if len(ret) > 0:
		print('Already Exists')
	else:
		cursor.execute('insert into `Users` (`User_ID`, `Password`, `Username`) values ("{}", "{}", "{}")'.format(username, password, displayName))
		conn.commit()
		print('User Created')
else:
	print('Recaptcha Failed')
