#!/usr/bin/python


#Internet Ressources : http://stackoverflow.com/questions/4589241/downloading-files-from-an-http-server-in-python
#		       http://docs.python.org/2/library/htmlparser.html

import getopt
import pycurl
import sys
import os
import StringIO
from HTMLParser import HTMLParser

#Variables
rez="1280x800"
imgDir=""
shuffle=False

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

try: #param stuff
        opts, args = getopt.getopt(sys.argv[1:],"s",["shuffle"])
except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

for o, a in opts: #set verbose mode
        if o in ("-s","--shuffle"):
                shuffle = True

b = StringIO.StringIO()
c=pycurl.Curl()
if shuffle:
	c.setopt(c.URL,'http://wlppr.com/shuffle')
else:
	c.setopt(c.URL,'http://wlppr.com/')
c.setopt(pycurl.WRITEFUNCTION, b.write)
c.perform()
c.close()
resp=b.getvalue()
parser = MyHTMLParser()
parser.feed(resp)
