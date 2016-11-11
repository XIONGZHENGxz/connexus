import os
import jinja2
import webapp2

JINJA_ENV=jinja2.FileSystemLoader(
loader=os.path.dirname(__file__),
extensions=['jinja2.ext.autoescape'],
autoescapte=True)

class viewAllStreamsPage(webapp2.RequestHandler):
	def get(self):
		template=JINJA_ENV.get_template('viewAllStream.html')
		streams=Stream.query().order(-Stream.createDate).fetch()
		template_values={
		"streams": streams,
		}
		self.response.write(template.render(template_values))


app=webapp2.WSGIApplication([('/viewall',viewAllStreamsPage),],debug=True)
		
