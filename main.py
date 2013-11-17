# coding: utf-8

import cherrypy
from jinja2 import Environment, FileSystemLoader
from ytsearch import RandomVideoBuilder
from database import computeAllVotes
from database import insertNewVote

host = 'localhost'
port = 8000
url = host+':'+str(port)

cherrypy.config.update({'server.socket_host': host,
                        'server.socket_port': port,
                       })

env = Environment(loader=FileSystemLoader(['templates', 'static']))
wikipediaPythonLink = "http://www.python.org/"

dictionary = open("words", 'r')
lDictionary = list(dictionary)
rvb = RandomVideoBuilder(lDictionary)

# main page
class Root:
    def __init__(self):
        self.userID = None
        self.status = None
        self.paricularVideoId = None

    @cherrypy.expose
    def index(self, videoId = None):
        tmpl = env.get_template('index.html')
        rvb.recompute()
        rvb.debug() # print things
        if videoId == None:
            videoId = rvb.getCurrentVideoId()
        self.setVideoId(videoId) # load in the page a particularVideo, http://localhost:8000/?videoId=f9O5F1eiIjI
        votes = computeAllVotes(videoId)
        print self.status
        return tmpl.render(title='Lose my time', currentVideoId=self.paricularVideoId, nextVideoId=rvb.getNextVideoId(),
        	videoTitle=rvb.getVideoTitle(), wikilink=wikipediaPythonLink, path='./', nbBored = votes[0], nbLiked = votes[1],
            connected=(self.status == 'connected'))

    @cherrypy.expose
    def concept(self):
        t = env.get_template('concept.html')
        print self.userID
        return t.render(title2 = 'Concept', path='../', userID = self.userID)   

    @cherrypy.expose
    def doVote(self, videoId = None, hasGotBored = None):
        # print "===>>>" + str(videoId) + " - " + str(hasGotBored)
        # insertNewElement([str(videoId),str(hasGotBored)])
        if self.userID != None and videoId != None and hasGotBored != None and self.status == 'connected':
            valid = insertNewVote(str(videoId), hasGotBored, self.userID) # return true if the insertion is valid (ie an update or an new entry)
            if valid:
                self.refreshVotes(videoId)
                
    @cherrypy.expose
    def updateFbInfo(self, userID = None, token = None, status = None):
        print "update user info"
        self.userID = userID
        self.status = status

    # use to refresh the number bored/liked
    def refreshVotes(self, videoId):
        computeAllVotes(videoId) # need a refresh dynamically
        self.index(videoId) # this does not refresh the page, does nothing....

    # setter
    def setVideoId(self, videoId):
        self.paricularVideoId = videoId

root = Root()
cherrypy.quickstart(root, '/', 'main.config')



