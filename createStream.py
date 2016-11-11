import webapp2
import os
from google.appengine.api import users
from google.appengine.ext import ndb
import jinja2
JINJA_ENV=jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True)
class Stream(ndb.Model):
	owner=ndb.UserProperty()
	tag=ndb.StringProperty(repeated=True)
	name=ndb.StringProperty()
	subscribers=ndb.StringProperty(repeated=True)
	createDate=ndb.DateTimeProperty(auto_now_add=True)
	dateOfLastPic=ndb.DateTimeProperty(auto_now_add=True)
	coverUrl=ndb.StringProperty()
	numOfPictures=ndb.IntegerProperty()
	@classmethod
	def get_myStreams(cls,user):
		return cls.query(owner==user).order(-cls.data).fetch()
	@classmethod
	def get_subStreams(cls,user):
		return cls.query(user in subscribers).order(-cls.data).fetch()


class createStreamPage(webapp2.RequestHandler):
	def get(self):
		template=JINJA_ENV.get_template('createStream.html')
		self.response.write("hello world")
		self.response.write(template.render())

class createStream(webapp2.RequestHandler):
	def post(self):
		stream=Stream()
		stream.name=self.request.get("stream_name")
		stream.owner=users.get_current_user
		stream.coverUrl.self.request.get("cover_image_url")
		stream.subscribers=self.request.get("subscribers").split(';')
		stream.numOfPictures=0;
		stream.tag=self.request.get("stream_tags").split(',')
		stream.put()


app=webapp2.WSGIApplication([('/createStream',createStreamPage),
('/create',createStream)],debug=True)
