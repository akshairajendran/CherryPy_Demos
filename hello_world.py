__author__ = 'arajendran'

import cherrypy

class HellowWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello World!"

if __name__ == '__main__':
    cherrypy.quickstart(HellowWorld())