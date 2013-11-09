import cherrypy
from jinja2 import Environment, FileSystemLoader
from ytsearch import RandomVideoBuilder
#import ytsearch

env = Environment(loader=FileSystemLoader('templates'))
wikipediaPythonLink = "http://en.wikipedia.org/wiki/Python_%28programming_language%29"

class Root:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('index.html')
        rvb = RandomVideoBuilder()
        return tmpl.render(title='Lose My Time', videoFrame=rvb.buildIFrameVideoFromUrl(), videoId=rvb.getVideoId(),
        	searchTerm=rvb.getSearchTerm(), wikilink=wikipediaPythonLink)

cherrypy.quickstart(Root())