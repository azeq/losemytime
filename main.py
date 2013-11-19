# coding: utf-8

import cherrypy
from user import User
from video import Video
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

# main page
class Root:
    def __init__(self):
        self.user = User()
        self.video = Video()
        self.rvb = RandomVideoBuilder(lDictionary)

    @cherrypy.expose
    def index(self, videoUUID = None):
        self.rvb.recompute()
        self.rvb.debug() # print things
        
        if videoUUID == None:
            videoUUID = self.rvb.getCurrentVideoId()
        self.video.setUUID(videoUUID)# load in the page a particularVideo, http://localhost:8000/?videoId=f9O5F1eiIjI

        votes = computeAllVotes(videoUUID)

        return env.get_template('index.html').render(
            pageTitle      = 'Lose my time', 
            currentVideoId = self.video.getUUID(), 
            nextVideoId    = self.rvb.getNextVideoId(),
            videoTitle     = self.rvb.getVideoTitle(), 
            wikilink       = wikipediaPythonLink, 
            path           ='./', 
            nbBored        = votes[0], 
            nbLiked        = votes[1],
            connected      = self.user.isValid())

    @cherrypy.expose
    def concept(self):
        return env.get_template('concept.html').render(
            pageTitle = 'Concept', 
            path      = '../')   

    @cherrypy.expose
    def doVote(self, hasGotBored = None):
        if self.user.isValid() and hasGotBored != None:
            valid = insertNewVote(str(self.video.getUUID()), hasGotBored, self.user.getUUID()) # return true if the insertion is valid (ie an update or an new entry)
            if valid:
                print "instertion done"
                
    @cherrypy.expose
    def updateFbInfo(self, userID = None, token = None, status = None):
        self.user.setUUID(userID)
        self.user.setValid(status == 'connected')

if __name__ == '__main__':
    root = Root()
    cherrypy.quickstart(root, '/', 'main.config')



