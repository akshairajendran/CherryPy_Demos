__author__ = 'arajendran'

import cherrypy
import random
import string

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return "Hello World!"

    @cherrypy.expose
    def generate(self):
        return ''.join(random.sample(string.hexdigits, 8))

if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())