#!/usr/bin/python
# coding: utf-8

import cherrypy
import urllib
from user import User
from video import Video
from jinja2 import Environment, FileSystemLoader
from ytsearch import RandomVideoBuilder
from database import computeAllVotes
from database import insertNewVote

host = 'localhost'
port = 8000
url = host+':'+str(port)

rootPath = './'

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
        time = self.rvb.compute()
        
        if videoUUID == None:
            videoUUID = self.rvb.getUuid()
        else:
            videoUUID = urllib.quote_plus(videoUUID) 
            if not self.rvb.isVideoExists(videoUUID):
                # for security but need to check that is a valid video otherwise a user can vote for bullshit
                # to do that, load the page and search for the ?v=videoUUID in the page. If it's present, the video is valid, otherwise it not
                # since if the uuid is not valid, youtube resend you to youtube.com and the video should not be on the page
                raise cherrypy.HTTPRedirect(rootPath) # redirect on home page

        self.video.setUUID(videoUUID)# load in the page a particularVideo, http://localhost:8000/?videoUUID=f9O5F1eiIjI

        votes = computeAllVotes(videoUUID)

        return env.get_template('index.html').render(
            pageURL        = url,
            pageTitle      = 'Lose my time', 
            currentVideoId = self.video.getUUID(), 
            nextVideoId    = self.rvb.getNuuid(),
            videoTitle     = self.rvb.getTitle(),
            time           = time, 
            wikilink       = wikipediaPythonLink, 
            path           = rootPath, 
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
                print "insertion done"
                
    @cherrypy.expose
    def updateFbInfo(self, userID = None, token = None, status = None):
        self.user.setUUID(userID)
        self.user.setValid(status == 'connected')

if __name__ == '__main__':
    root = Root()
    cherrypy.quickstart(root, '/', 'main.config')



