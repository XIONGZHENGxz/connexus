import os
import webapp2
import jinja2 
import urllib
from stream import Stream

JINJA_ENV=jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class searchPage(webapp2.RequestHandler):
	def post(self):
		query=self.request.get('searchstream')	
		print query
		query_url=urllib.urlencode({'query': query})
		streams=Stream.query(Stream.name==query).order(Stream.view_count).fetch()
		template_values={
		'streams': streams,
		}
		template=JINJA_ENV.get_template('search.html')
		self.response.write(template.render(template_values))


app=webapp2.WSGIApplication([('/searchStreams',searchPage),],debug=True)


