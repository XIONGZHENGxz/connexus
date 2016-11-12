import os
import jinja2
import webapp2
from datetime import datetime,timedelta
from stream import Stream

JINJA_ENV=jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class trendingPage(webapp2.RequestHandler):
	def get(self):
		streams=Stream.query().order(Stream.view_count).fetch()
		template_values={
		'top_streams': streams
		}
		template=JINJA_ENV.get_template('trending.html')
		self.response.write(template.render(template_values))


app=webapp2.WSGIApplication([('/trending',trendingPage),])
