import webapp2
import os
import jinja2

JINJA_ENV=jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class managementPage(webapp2.RequestHandler):
	def get(self):
		template=JINJA_ENV.get_template('management.html')
	
class delete(webapp2.RequestHandler):
	def post(self):
		
class unsubscribe(webapp2.RequestHandler):
	def post(self):

app=webapp2.WSGIApplication([('/management',managementPage),],debug=True)
