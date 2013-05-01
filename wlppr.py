#!/usr/bin/python


#Internet Ressources : http://stackoverflow.com/questions/4589241/downloading-files-from-an-http-server-in-python
#		       http://docs.python.org/2/library/htmlparser.html

import pycurl
import sys
import os
import StringIO
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser): 
    def handle_data(self, data):
	if 'var base_url' in data:
		base_url=data.split("'")
		url="http://wlppr.com/"+base_url[1]+"."+rez+".jpg";
		nameArray=base_url[1].split('/')
		name=imgDir+nameArray[-1]+"."+rez+".jpg";
		if os.path.isfile(name) == False:
			imgFile=open(name,"wb")
			img=pycurl.Curl()
			img.setopt(img.URL,url)
			img.setopt(img.WRITEDATA,imgFile)
			img.perform()
			imgFile.close()
			img.close()
			print "Downloaded "+name
		else:
			print "File already exists"

b = StringIO.StringIO()
c=pycurl.Curl()
rez="1280x800"
imgDir="/home/sybix/Images/wallpaper/"
#c.setopt(c.URL,'http://wlppr.com/')
c.setopt(c.URL,'http://wlppr.com/2013/04/28/the-hobbit')
c.setopt(pycurl.WRITEFUNCTION, b.write)
c.perform()
c.close()
resp=b.getvalue()
parser = MyHTMLParser()
parser.feed(resp)
