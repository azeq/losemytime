# coding: utf-8

import cherrypy
from jinja2 import Environment, FileSystemLoader
from ytsearch import RandomVideoBuilder
from vote import insertNewElement

cherrypy.config.update({'server.socket_host': '127.0.0.1',
                        'server.socket_port': 9292,
                       })

env = Environment(loader=FileSystemLoader(['templates', 'static']))
wikipediaPythonLink = "http://www.python.org/"

dictionary = open("words", 'r')
lDictionary = list(dictionary)
rvb = RandomVideoBuilder(lDictionary)

# main page
class Root:
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
		return t.render(title2 = 'Concept', pathStyle='../', url='../')

    @cherrypy.expose
    def vote(self, videoId, hasGotBored):
        insertNewElement([videoId,hasGotBored])
        return self.index()

    @cherrypy.expose
    def doVote(self, videoId = None, hasGotBored = None):
        print "$$$$$$$$$$$$$$$$ Vottttttttttttttttteeeeeeeee"
        print type(str(videoId))
        print videoId
        print type(hasGotBored)
        print hasGotBored
        insertNewElement([str(videoId),str(hasGotBored)])
    

root = Root()
cherrypy.quickstart(root, '/', 'main.config')