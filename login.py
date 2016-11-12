import jinja2
import webapp2
import os
from google.appengine.api import users

JINJA_ENV=jinja2.Environment(loader=jinja2.FileSystemLoader(
os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class loginPage(webapp2.RequestHandler):
	def get(self):
		user=users.get_current_user()
		if user:
			url=users.create_logout_url('/')
			url_text="Logout"
		else:
			url=users.create_login_url('/home')
			url_text="Login"
		template_values={
		'url': url,
		'url_text': url_text
		}
		template=JINJA_ENV.get_template('mainPage.html')
		self.response.write(template.render(template_values))
class homePage(webapp2.RequestHandler):
	def get(self):
		template=JINJA_ENV.get_template('homePage.html')
		self.response.write(template.render())

app=webapp2.WSGIApplication([('/',loginPage),('/home',homePage)],debug=True)

