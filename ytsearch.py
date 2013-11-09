import urllib
import sys
import re
import random

collection = ['dolls', 'booba']

class RandomVideoBuilder:

    def __init__(self):
        self.term = collection[random.randint(0,1)]
        self.id = "00000"

    def buildIFrameVideoFromUrl(self):
        query = "http://www.youtube.com/results?search_query="+self.term
        print query

        yTUBE = urllib.urlopen(query).read()
        sTUBE = str(yTUBE)

        #href="/watch?v=RsltR02GNZE"
        tmp_mat = re.compile("<a href=\"/watch\?v=(.+?)(&(.+?))*\" ") #pattern to match for finding a video link
        match = re.search(tmp_mat, sTUBE) #retreive only one
        if match:
            result = match.group(1)
            self.id = result
            embeddeVideo = "<iframe width=\"420\" height=\"315\" src=\"//www.youtube.com/embed/"+result+"\" frameborder=\"0\" allowfullscreen></iframe>"
            return embeddeVideo

        else:
            return "no result"

    def getSearchTerm(self):
        return self.term

    def getVideoId(self):
        return self.id

