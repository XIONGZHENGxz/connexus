import urllib
import webapp2
import os
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext import db
from google.appengine.api import mail
import jinja2
from stream import Stream

JINJA_ENV=jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class createStreamPage(webapp2.RequestHandler):
	def get(self):
		template=JINJA_ENV.get_template('createStream.html')
		self.response.write(template.render())

class createStream(webapp2.RequestHandler):
	def post(self):
		if not users.get_current_user:
			self.redirect(users.create_login_url(self.request.referer))
		else:
			stream=Stream()
			stream.name=self.request.get("stream_name")
			stream.owner=users.get_current_user()
			stream.coverUrl=self.request.get("cover_image_url")
			stream.subscribers=self.request.get("subscribers").split(';')
			stream.numOfPictures=0;
			stream.tag=self.request.get("stream_tags").split(',')
			email_body=self.request.get("email_content")
			stream.url=urllib.urlencode({'stream_name':stream.name})
			print stream.url
			stream.put()
			for subscriber in stream.subscribers:
				send_mail("zhengxionguta@gmail.com",subscriber,email_body)
			self.redirect(self.request.referer)

def send_mail(sender_add,receiver_add,email_body):
	mail.send_mail(sender=sender_add,
		to=receiver_add,
		subject="share new stream",
		body=email_body)

def generate_stream_url(name):
	id_chars=string.ascii_letters+string.digits
	rand=random.SystemRandom()
	random_url= ''.join([rand.choice(id_chars) for i in range(42)])
	random_url='https://'+random_url+'%'+name+'%'
	return random_url
		

app=webapp2.WSGIApplication([('/createstream',createStreamPage),('/create',createStream)],debug=True)
