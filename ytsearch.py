# coding: utf-8

import urllib
import re
import random
import cgi
# import pdb # for debugging

class RandomVideoBuilder:

    def __init__(self, listDict):
        self.listDict = listDict #random.choice(collection) #pick randomly a word
        self.uuid = None
        self.nuuid = None

    # uuid e.g RsltR02GNZE
    def videoPage(self, uuid):
        query = u'http://www.youtube.com/watch?v={}'.format(uuid)
        return str(urllib.urlopen(query).read())
    
    # parameter e.g Eminem
    # page = a digit, 1 by default
    def search(self, parameter, page = 1):
        query = u'http://www.youtube.com/results?search_query={}&page={}'.format(parameter, page)
        return str(urllib.urlopen(query).read())

    # retrieve all video uuid of a source page content
    def parsePage(self, content):
        pattern = "<a href=\"/watch\?v=([\w\-]{11})\" "
        return re.findall(pattern, content)

    def randomVideo(self):
        i = 0
        # 10 tries
        while i < 10: 
            term = random.choice(self.listDict)
            result1 = self.parsePage(self.search(term))
            if len(result1) > 0:
                # try from first to last page (1 to 50)
                N = random.randint(2, 50)
                while N > 1:
                    resultN = self.parsePage(self.search(term, N))
                    if result1 != resultN and len(resultN) > 0:
                        return random.choice(resultN)
                    else:
                        N -= 1
                return random.choice(result1)
            i += 1
        return u'RsltR02GNZE' # send something

    def compute(self):
        if self.nuuid == None:
            self.uuid = self.randomVideo() # for the initialization
        else:
            self.uuid = self.nuuid # swap id
        self.nuuid = self.randomVideo() # and recompute the next one    

    def getTitle(self):
        sTUBE = self.videoPage(self.uuid)
        tmp_mat = re.compile("<span id=\"eow-title\" (.+?) title=\"(.+?)\">") #pattern to match for finding the title of the video
        match = re.search(tmp_mat, sTUBE) #retreive only one
        if match:
            title = match.group(2)
            return self.escape(title) 
        else:
            return self.uuid  

    def isVideoExists(self, uuid):
        pattern = "\"http\:\/\/www\.youtube\.com\/watch\?v=([\w\-]{11})\""
        result = re.findall(pattern, self.videoPage(uuid))
        return uuid in result
    
    def getUuid(self):
        return self.uuid

    def getNuuid(self):
        return self.nuuid   

    # to desactivate <,& characters... and to avoid error with non ascii character such as ö,é...
    def escape(self, s):
        u = unicode(s, "utf-8")
        sEscaped = cgi.escape(u).encode('ascii', 'xmlcharrefreplace')   
        return sEscaped  

    # to see raw result in the terminal
    def debug(self):
        print '===>>> Current Id: '+self.getUuid()
        print '===>>> Next Id: '+self.getNuuid()
        print '===>>> Title: '+self.getTitle() 



