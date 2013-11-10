import cherrypy
from jinja2 import Environment, FileSystemLoader
from ytsearch import RandomVideoBuilder

env = Environment(loader=FileSystemLoader(['templates', 'static']))
wikipediaPythonLink = "http://www.python.org/"

dictionary = open("words", 'r')
lDictionary = list(dictionary)
rvb = RandomVideoBuilder(lDictionary)

class Root:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('index.html', 'head.html')
        rvb.recompute()
        return tmpl.render(title='Lose my time', currentVideoId=rvb.getCurrentVideoId(), nextVideoId=rvb.getNextVideoId(),
        	videoTitle=rvb.getVideoTitle(), wikilink=wikipediaPythonLink)

cherrypy.quickstart(Root(), '/', 'main.config')