import sys
import urllib
from BeautifulSoup import *

#Default stop # is 12231 (Summit & Essex)
njtURL = "http://mybusnow.njtransit.com/bustime/wireless/html/eta.jsp?route=---&direction=---&displaydirection=---&stop=---&findstop=on&selectedRtpiFeeds=&id="
#print "SYS Len:", len(sys.argv), "sys.argv[0] ", sys.argv[0]

if len(sys.argv) > 1:
    njtURL += sys.argv[1]
else:
    njtURL += "12231"

print njtURL

html = urllib.urlopen(njtURL).read()
soup = BeautifulSoup(html)
tags = soup('b')

print tags
