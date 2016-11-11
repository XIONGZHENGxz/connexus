import webapp2
import os
import jinja2

JINJA_ENV=jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class managementPage(webapp2.RequestHandler):
	def get(self):
		template=JINJA_ENV.get_template('management.html')
		self.response.write("hellow world")
		mystreams=Stream.get_myStreams(users.get_current_user)
		substreams=Steam.get_subStreams(users.get_current_user)
		template_values={
		"Mystreams": mystreams,
		"subStreams": substreams
		}
		self.response.write(template.render(template_values))

	
class delete(webapp2.RequestHandler):
	def post(self):
		
class unsubscribe(webapp2.RequestHandler):
	def post(self):

app=webapp2.WSGIApplication([('/management',managementPage),],debug=True)
