import jinja2
import webapp2
import os
from google.appengine.api import users

JINJA_ENV=jinja2.Environment(loader=jinja2.FileSystemLoader(
os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class testPage(webapp2.RequestHandler):
	def get(self):
		print "xz"
		self.response.content_type='text/plain'
		self.response.write('helloworld...')

app=webapp2.WSGIApplication([('/test',testPage),],debug=True)

