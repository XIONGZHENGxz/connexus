import os
import jinja2
import webapp2
from stream import Stream

JINJA_ENV=jinja2.Environment(loader=jinja2.FileSystemLoader(
os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class viewAllStreamsPage(webapp2.RequestHandler):
	def get(self):
		template=JINJA_ENV.get_template('viewAllStream.html')
		streams=Stream.query().order(-Stream.createDate).fetch()
		template_values={
		"streams": streams,
		}
		self.response.write(template.render(template_values))


app=webapp2.WSGIApplication([('/viewAll',viewAllStreamsPage),],debug=True)
		
