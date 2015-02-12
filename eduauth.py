#!/usr/bin/python

import sys
import urllib
import urllib2



def auth(login, password, verbose):
	proxy_handler = urllib2.ProxyHandler({})
	opener = urllib2.build_opener(proxy_handler)
	urllib2.install_opener(opener)
	headers = {'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'}
	values = {
        'buttonClicked':'4',
        'redirect_url':'https://edu.tatar.ru',
        'err_flag': '0',
        'username':login,
        'password' : password
		}
	data = urllib.urlencode(values)
	#req = urllib2.Request('https://wifiauth.tatar.ru/login.html', data, headers)
	req = urllib2.Request('http://edu.tatar.ru/', data, headers)
	if verbose:
		response = urllib2.urlopen(req)
		text = response.read()
		print text
	return 1


values = [0, 0, 0]
hasValues = [0, 0]
# values[0] - login, values[1] - password

if __name__ == "__main__":
	if len(sys.argv) == 1:
		print " Error \n Type eduproxy.py -h"
		exit()
	for param in sys.argv:
		if param == "-h":
			print "Help: \n -h  help \n -u Username \n -p Password\
			\n-v Verbose (print HTML)\nE.g: \n eduauth.py -u=4702000300 -p=password -v"
			exit()
		if param == "-v":
			values[2] = 1
			continue
		paramName = param[0:2]
		paramValue = param[3:]
		if paramName == "-p":
			values[1] = paramValue
			hasValues[1] = 1
		elif paramName == "-u":
			values[0] = paramValue
			hasValues[0] = 1

if (sum(hasValues) != 2):
	print " Error: \nNot enough params\nTry eduproxy.py -h"
	exit()
print int(auth(values[0], values[1], values[2]))
