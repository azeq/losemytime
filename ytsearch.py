import urllib
import sys
import re

sys.argv.append("cars")
sys.argv.append("cars")

if len(sys.argv) > 1:
    term = sys.argv[1] #the url from command
    query = "http://www.youtube.com/results?search_query="+term
    print query

    yTUBE = urllib.urlopen(query).read()
    sTUBE = str(yTUBE)

    #href="/watch?v=RsltR02GNZE"
    tmp_mat = re.compile("<a href=\"/watch\?v=(.+?)\" ") #pattern to match for finding a video link
    match = re.search(tmp_mat, sTUBE) #retreive only one
    #matchAll = re.findall(tmp_mat, sTUBE)
    if match:
        result = match.group(1)
        embeddeVideo = "<iframe width=\"420\" height=\"315\" src=\"//www.youtube.com/embed/\""+result+"\" frameborder=\"0\" allowfullscreen></iframe>"
        print embeddeVideo
    #    for res in matchAll:
    #        print res

    else:
        print "no result"

else:
    print "indicate term"
