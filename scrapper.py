#!/usr/bin/env python
import urllib2
from BeautifulSoup import BeautifulSoup

def GetTitle(url):
	try:
		web = urllib2.urlopen(url)
	except urllib2.URLError as e:
		print e
	try:
		 soup = BeautifulSoup(web.read(), 'html.parser')
		 title = soup.body.h1
	except AttributeError as e:
		 return None
url = "http://network-class.net"
title = GetTitle(url)
if title == None:
	print "There is no such title"
else:
	print title
