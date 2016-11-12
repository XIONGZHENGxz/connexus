import webapp2
import os
import jinja2
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import ndb,db,blobstore
from stream import *
from google.appengine.api import users,images

JINJA_ENV=jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class managementPage(webapp2.RequestHandler):
	def get(self):
		template=JINJA_ENV.get_template('management.html')
		mystreams=Stream.get_myStreams(users.get_current_user())
		substreams=getSubscribers(users.get_current_user())
		template_values={
		"Mystreams": mystreams,
		"subStreams": substreams
		}
		self.response.write(template.render(template_values))
	
class deleteStream(webapp2.RequestHandler):
	def post(self):
		referer=self.request.referer
		delete_streams_name=self.request.get_all('delete_status')
		print delete_streams_name
		streams=Stream.query(Stream.name.IN(delete_streams_name),Stream.owner==users.get_current_user()).fetch()
		for stream in streams:
			images=db.GqlQuery("SELECT * FROM Image WHERE ANCESTOR IS :1",db.Key().from_path('Stream',stream.name))
			db.delete(images)

		ndb.delete_multi(ndb.put_multi(streams))
		self.redirect(referer)

class unsubscribeStream(webapp2.RequestHandler):
	def post(self):
		referer=self.request.referer
		unsubscribe_streams_name=self.request.get_all('unsubscribe_status')
		streams=Stream.query(Stream.name.IN(unsubscribe_streams_name)).fetch()
		for stream in streams:
			stream.subscribers.remove(users.get_current_user().email())
		self.redirect(referer)


app=webapp2.WSGIApplication([('/management',managementPage),
('/deletestream',deleteStream),('/unsubscribestream',unsubscribeStream),],
debug=True)
