import jinja2
JINJA_ENV=jinja2.Environment(loader=jinja2.FileSystemLoader(os_path_dirname(__file__)),extensions=['jinja2.ext.autoescape]')
class loginPage(webapp2.RequestHandler):
	
