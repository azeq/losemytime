# coding: utf-8

import cherrypy
from jinja2 import Environment, FileSystemLoader
from ytsearch import RandomVideoBuilder
from vote import insertNewElement
from database import insertNewVote

port = 8000
cherrypy.config.update({'server.socket_host': '127.0.0.1',
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
        self.stat = None

    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('index.html')
        rvb.recompute()
        rvb.debug() # print things
        return tmpl.render(title='Lose my time', currentVideoId=rvb.getCurrentVideoId(), nextVideoId=rvb.getNextVideoId(),
        	videoTitle=rvb.getVideoTitle(), wikilink=wikipediaPythonLink, url='/')

    @cherrypy.expose
    def concept(self):
        t = env.get_template('concept.html')
        print self.userID
        return t.render(title2 = 'Concept', pathStyle='../', url='../', userID = self.userID)   

    @cherrypy.expose
    def doVote(self, videoId = None, hasGotBored = None):
        print "===>>>" + str(videoId) + " - " + str(hasGotBored)
        insertNewElement([str(videoId),str(hasGotBored)])
        if self.userID != None and videoId != None and hasGotBored != None:
            insertNewVote(str(videoId), hasGotBored, self.userID)
    
    @cherrypy.expose
    def updateFbInfo(self, userID = None, token = None, stat = None):
        print "update user info"
        self.userID = userID
        self.stat = stat

root = Root()
cherrypy.quickstart(root, '/', 'main.config')



