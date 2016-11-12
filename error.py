import os 
import jinja2
import webapp2

class errorPage(webapp2.RequestHandler):
	def get(self):
		error_info=re.findall('error=(.*)',self.request.url)
		template_values={
		'error_info': error_info,
		}
		template=JINJA_ENV.get_template('error.html')
		self.response.write(template.render(template_values))

app=webapp2.WSGIApplication([('/error.*',errorPage),],debug=True)

