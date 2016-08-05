#!/usr/bin/env python
import urllib2
from beautifulsoup import BeautifulSoup

try:
	html  = urlopen("http://network-class.net")
except HTTPError as e:
	print e
