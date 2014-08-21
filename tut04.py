__author__ = 'arajendran'

import cherrypy
import random
import string

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
        <head></head>
        <body>
            <form method="post" action="generate">
                <input type="text" value="8" name="length"/>
                <button type="submit">Click yo</button>
            </form>
        </body>
        </html>"""

    @cherrypy.expose
    def generate(self, length=8):
        return ''.join(random.sample(string.hexdigits, int(length)))

if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())