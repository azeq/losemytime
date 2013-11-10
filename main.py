# coding: utf-8

import cherrypy
from jinja2 import Environment, FileSystemLoader
from ytsearch import RandomVideoBuilder

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

root = Root()
cherrypy.quickstart(root, '/', 'main.config')