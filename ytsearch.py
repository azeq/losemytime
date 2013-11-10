import urllib
import sys
import re
import random

class RandomVideoBuilder:

    def __init__(self, listDict):
        self.listDict = listDict #random.choice(collection) #pick randomly a word
        self.currentId = ""
        self.nextId = ""

    def buildIFrameVideoFromUrl(self):
        i = 0
        # only 10 tries
        while i < 10:
            term = random.choice(self.listDict)
            query = "http://www.youtube.com/results?search_query="+term

            yTUBE = urllib.urlopen(query).read()
            sTUBE = str(yTUBE)

            #href="/watch?v=RsltR02GNZE"
            tmp_mat = re.compile("<a href=\"/watch\?v=(.+?)(&(.+?))*\" ") #pattern to match for finding a video uuid
            match = re.search(tmp_mat, sTUBE) #retreive only one
            if match:
                return match.group(1)
            i += 1

        return "The algorithm does not want you to lose time anymore."

    def getCurrentVideoId(self):
        return self.currentId

    def getNextVideoId(self):
        return self.nextId   

    def recompute(self):
        if self.nextId == "":
            self.currentId = self.buildIFrameVideoFromUrl() # for the initialization
        else:
            self.currentId = self.nextId # swap id
        self.nextId = self.buildIFrameVideoFromUrl() # and recompute the next one    

    def getVideoTitle(self):
        query = "http://www.youtube.com/watch?v="+self.currentId
        yTUBE = urllib.urlopen(query).read()
        sTUBE = str(yTUBE)
        tmp_mat = re.compile("<span id=\"eow-title\" (.+?) title=\"(.+?)\">") #pattern to match for finding the title of the video
        match = re.search(tmp_mat, sTUBE) #retreive only one
        if match:
            title = match.group(2)
            return title
        else:
            return self.currentId        

if __name__=='__main__':
   print RandomVideoBuilder().buildIFrameVideoFromUrl()       

